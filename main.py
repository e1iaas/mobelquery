
import spacy
import pandas as pd
from filter import process_text
from prepare import prepare_for_embeddings
from embed import create_embeddings_local, analyze_data
from semantic_search import semantic_search
from fetch import fetch_products
from utils import save_to_csv
from analyze import analyze_text_words

from dotenv import load_dotenv
import os

load_dotenv()


base_url = 'https://app.partnerboost.com/api.php?mod=datafeed&op=list'
token = os.getenv("API_KEY")
limit = 100
brand_id = 96699

params_obj = {
        'token': token,
        'type': 'JSON',
        'brand_type': 'DTC',
        'brand_id': brand_id,
        'limit': limit,
    }


def run_pipeline():
    """RUN ETL pipeline"""
    print("\n === SEMANTIC SEARCH DATA PIPELINE ====\n")

    #fetch data
    raw_products = fetch_products(base_url,params_obj)
    if not raw_products:
        print("No products fetched")
        return
    save_to_csv(raw_products, "raw_products.csv")

    #prepare data for embeddings
    df = prepare_for_embeddings(raw_products)
    df.to_csv("products_for_embeddings.csv", index=False)

    #clean text
    nlp = spacy.load("en_core_web_sm")
    df["combined_text_clean"] = df["combined_text"].apply(
        lambda text: process_text("whitelist.txt", "blacklist.txt", text, nlp)
    )
    if 'combined_text_cleaned' in df.columns:
        df = df.drop(columns=['combined_text_cleaned'])

    df.to_csv("products_cleaned_final.csv", index=False)


    #analyze text
    df_cleaned = pd.read_csv("products_cleaned_final.csv")
    analyze_text_words(df_cleaned)

    #Create embeddings
    df = create_embeddings_local("products_cleaned_final.csv")

    return df

if __name__ == "__main__":
    df = run_pipeline()

    # 5️⃣ Semantic search examples
    semantic_search("dining chair with metal base", top_k=3)
    semantic_search("modular corner seat", top_k=3)
    semantic_search("wood sofa", top_k=3)
