

from fetch import fetch_products
from normalize import normalize_raw_product
from regex_clean import pre_process_regex, post_process_regex, chunk_text
from load_from_csv import load_from_csv
from semantic_spacy import run_semantic_score
from embed import create_embeddings_local, analyze_data


from write_semantic_products import write_semantic_products
from utils import save_to_csv
from dotenv import load_dotenv
import os
import pandas as pd
from sentence_transformers import SentenceTransformer 


from query import run_query


#load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")


base_url = 'https://app.partnerboost.com/api.php?mod=datafeed&op=list'
token = os.getenv("API_KEY")
limit = 100
brand_id = 134627

params_obj = {
        'token': token,
        'type': 'JSON',
        'brand_type': 'DTC',
        'brand_id': brand_id,
        'limit': limit,
    }


def run_pipeline(model):
    """RUN ETL pipeline"""
    print("\n === SEMANTIC SEARCH DATA PIPELINE ====\n")

    #fetch data
    """
    raw_products = fetch_products(base_url,params_obj)
    if not raw_products:
        print("No products fetched")
        return

    #save_to_csv(raw_products, "raw_products.csv")
    """

    raw_products = load_from_csv("raw_products.csv")
    #normalized data
    normalized_products = []
    all_rows = []

    for raw in raw_products:
        normalized = normalize_raw_product(raw)
        if normalized:
            normalized_products.append(normalized)

    for product in normalized_products:
        raw_description = product.product_raw["description"]
        raw_sku = product.product_raw["sku"]

        if not raw_description or not raw_sku:
            continue


    #access raw description and attach sku from the raw data


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

        top_chunks = sorted(results, key=lambda x: x["score"], reverse = True)[:2]

        for c in top_chunks:

            rows = {
                "sku": product.product_sku,
                "chunk_text": c["chunk"],
                "semantic_score": c["score"],
                "category": product.product_category,
                "price_tier": product.price_tier

            }
            all_rows.append(rows)

    write_semantic_products("semantic_products.csv",all_rows)

    final_rows = []
    for row in all_rows:
        if row["semantic_score"] < 7:
            continue
        
        final_rows.append({
            "sku": row["sku"],
            "chunk_text": row["chunk_text"],
            "semantic_score": row["semantic_score"],
            "category": row["category"],
            "price_tier": row["price_tier"]
        })

    write_semantic_products("final_semantic_product.csv", final_rows)

    create_embeddings_local("final_semantic_product.csv")
    

    run_query(model)

        #STORE semanitc chunks

if __name__ == "__main__":
    df = run_pipeline(model)

