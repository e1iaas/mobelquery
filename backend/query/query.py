print("IMPORTING QUERY")
import faiss
import numpy as np
import pandas as pd

from search.loader import Loader



#add a limit to pagination. k=2
#handle empty results.   if( I ):
search_loader = Loader()

def run_query(query):
    

    model = search_loader.model
    index = search_loader.index
    df = search_loader.df_stacked_data
    raw_index = search_loader.df_raw_index_sku

    print("encoding model query")
    query_vec = model.encode([query]).astype("float32")


    print("faiss search")
    D,I = index.search(query_vec, k=10)

    results = {}

  
    for idx in I[0]:
        row = df.iloc[idx]
        sku = row["sku"]

        raw_row = raw_index[sku]
        raw_url = raw_row["url"]
        raw_img = raw_row["image"]
        raw_availability = raw_row["availability"]
        raw_price = raw_row["price"]
        raw_currency = raw_row["currency"]

        if sku not in results:
            sku_rows = df[df["sku"] == sku]

            name_text = sku_rows[sku_rows["source_type"] == "name"]["source_text"].values
            desc_text = sku_rows[sku_rows["source_type"] == "description"]["source_text"].values

            results[sku] = {
                "name": name_text,
                "description": desc_text,
                "url": raw_url,
                "image": raw_img,
                "available": raw_availability,
                "price": raw_price,
                "currency": raw_currency
            }

    final_response = {
        "query": query,
        "count": len(results),
        "results": list(results.values())
    }
    print("return final result")
    return final_response



