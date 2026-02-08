

from extract.fetch import fetch_products
from transform.normalize import normalize_raw_product
from transform.regex_clean import pre_process_regex, post_process_regex, chunk_text
from utils.load_from_csv import load_from_csv
from transform.semantic.semantic_spacy import run_semantic_score
from transform.embed import create_embeddings_local, analyze_data


from utils.write_semantic_products import write_semantic_products
from utils.utils import save_to_csv
from dotenv import load_dotenv
import os
import pandas as pd


#load_dotenv()


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

FIELDNAMES_SEMANTIC = [
    "sku",
    "chunk_text",
    "semantic_score",
    "category",
    "price_tier",
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

    #fetch data
    """
    raw_products = fetch_products(base_url,params_obj)
    if not raw_products:
        print("No products fetched")
        return

    #save_to_csv(raw_products, "raw_products.csv")
    """

    raw_products = load_from_csv("etl/data/raw/raw_products.csv")

    #normalized data
    normalized_products = []

    #semantic data stored here before final filtering
    all_rows = []

    #product name and other data from producs
    product_name_products = []

    stacked_product_names = []

    

    for raw in raw_products:
        normalized = normalize_raw_product(raw)
        if normalized:
            normalized_products.append(normalized)

    for product in normalized_products:
        raw_description = product.product_raw["description"]
        raw_sku = product.product_raw["sku"]

        raw_name = product.product_name
        raw_brand = product.product_brand
        raw_availability = product.availability

        if not raw_description or not raw_sku:
            continue

    #TO DO: EXTRACT RAW NAME AND VALUABLE META DATA INDEX THE PRODUCT NAME
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
                "category": product.product_category,
                "price_tier": product.price_tier

            }
            all_rows.append(rows)

    write_semantic_products("semantic_products.csv",all_rows, FIELDNAMES_SEMANTIC)

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

        

        
    #final semantic products
    write_semantic_products("final_semantic_product.csv", final_rows, FIELDNAMES_SEMANTIC)

    
    write_semantic_products("final_semantic_product_names.csv", product_name_products, FIELDNAMES_PRODUCT)

    #create embeddings
    create_embeddings_local("final_semantic_product.csv","chunk_text", "embedded_products_final.csv")

    create_embeddings_local("final_semantic_product_names.csv", "name", "embedded_embeddings_final.csv")
    
    df_names = pd.read_csv("embedded_embeddings_final.csv")
    df_desc = pd.read_csv("embedded_products_final.csv")

    df_names = df_names.rename(columns={
        "name": "source_text",
        "embeddings": "source_embeddings",
    })

    df_desc = df_desc.rename(columns={
        "chunk_text": "source_text",
        "embeddings": "source_embeddings",
    })

    df_names["source_type"] = "name"
    df_desc["source_type"] = "description"

    cols = ["sku", "source_type", "source_text", "source_embeddings"]

    df_names = df_names[cols]
    df_desc = df_desc[cols]

    stacked_df = pd.concat([df_names, df_desc], ignore_index=True)

    
    stacked_df.to_csv("stacked_product_embeddings.csv")

if __name__ == "__main__":
    df = run_pipeline()

