import faiss
import numpy as np
import pandas as pd
import ast #so i eval doesnt literally run code only parses data types

from sentence_transformers import SentenceTransformer 
from django.apps import apps


def run_query(query):
    #loaded model
    #laoded csv
    #encoded vectors
    #reformat vectors from strings to array of numbers
    #load faiss
    #reutrned result
    print("loading model")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("loading csv")
    product_embeddings = pd.read_csv("product_embeddings.csv")
    raw_product = pd.read_csv("raw_products.csv")
    raw_index = raw_product.set_index("sku").to_dict(orient="index")

    embeddings = np.array(product_embeddings["embeddings"].apply(ast.literal_eval).tolist(), dtype="float32")

    query_vec = model.encode([query]).astype("float32")

    diemension = len(embeddings[0])

    index = faiss.IndexFlatL2(diemension)

    index.add(embeddings)

    D,I = index.search(query_vec, k=2)

    results = []

    for idx in I[0]:
        product_embedding = product_embeddings.iloc[idx]
        sku = product_embedding["sku"]
        chunk = product_embedding["chunk_text"]

        raw_row = raw_index[sku]
        raw_name = raw_row["name"]
        raw_url = raw_row["url"]

        results.append({
            "name": raw_name,
            "chunk": chunk,
            "url": raw_url
        })

    return results



"""
def run_query( query):
    print("run_query called")
    lookups = apps.get_app_config("lookups")
    print("lookups loaded")

    results = []
    #wncode the query here
    query_vec = lookups.model.encode([query]).astype("float32")
    print("encoded query")

    D,I = lookups.index.search(query_vec, k=5)
    print("faiss search done")

    for idx in I[0]:
        sku = lookups.faiss_index_to_sku[idx]
        product = lookups.df_raw_index_sku[sku]
        results.append(product)

    return results

"""