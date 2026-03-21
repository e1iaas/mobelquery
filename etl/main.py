

from extract.fetch import fetch_products
from transform.normalize import normalize_raw_product
from transform.regex_clean import pre_process_regex, post_process_regex, chunk_text
from transform.semantic.semantic_spacy import run_semantic_score
from transform.embed import create_embeddings_local, analyze_data
from extract.scrape import scrape_all

from utils.write_semantic_products import write_semantic_products
from utils.utils import save_to_csv
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from itertools import islice


#load_dotenv()

PIPELINE_CONFIG = {
    "semantic_scoring": False,
    "max_pages": 5,
    "categories": ["sofas"]
}


FIELDNAMES_SEMANTIC = [
    "sku",
    "chunk_text",
    "semantic_score",
]

FIELDNAMES_PRODUCT = [
    "sku",
    "name",
    "brand",
    "available",
]

def run_pipeline():
    """RUN ETL pipeline"""
    print("\n === SEMANTIC SEARCH DATA PIPELINE ====\n")


    #normalized data
    normalized_products = []

    #semantic data stored here before final filtering
    all_rows = []



    scraped_data = scrape_all()
   
    

    for raw in scraped_data:
        print(type(raw))
        normalized = normalize_raw_product(raw)
        if normalized:
            normalized_products.append(normalized)

    for product in normalized_products:
        raw_description = product.product_raw["description"]
        raw_sku = product.product_sku

        raw_name = product.product_name
        raw_brand = product.product_brand
        raw_availability = product.availability

        if not raw_description or not raw_sku:
            continue

        processed_name = pre_process_regex(raw_name)

        product_name_products.append({
            "sku": raw_sku, 
            "name": processed_name, 
            "brand": raw_brand, 
            "available": raw_availability
            })



    #clean raw description
        pre_description_regex = pre_process_regex(raw_description)
        post_description_regex = post_process_regex(pre_description_regex)

    #chunk
        chunked_text = chunk_text(post_description_regex)

        results = []

        for chunk in chunked_text:
            score,reasons = run_semantic_score(chunk)

            results.append({
                "chunk": chunk,
                "score": score,
            })

        top_chunks = sorted(results, key=lambda x: x["score"], reverse = True)[:1]

        for c in top_chunks:
            rows = {
                "sku": product.product_sku,
                "chunk_text": c["chunk"],
                "semantic_score": c["score"],

            }
            all_rows.append(rows)

    write_semantic_products("semantic_products.csv",all_rows, FIELDNAMES_SEMANTIC)
   
    final_rows = []
    
    if PIPELINE_CONFIG["semantic_scoring"]:
        for row in all_rows:
            if row["semantic_score"] < 7:
                continue
            
            final_rows.append({
                "sku": row["sku"],
                "chunk_text": row["chunk_text"],
                "semantic_score": row["semantic_score"],
            })

        
    #final semantic products
    write_semantic_products("final_semantic_product.csv", final_rows, FIELDNAMES_SEMANTIC)

    
   

if __name__ == "__main__":
    df = run_pipeline()

