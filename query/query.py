import faiss
import numpy as np
import pandas as pd
import ast #so i eval doesnt literally run code only parses data types


def run_query(model):

    df = pd.read_csv("product_embeddings.csv")
    #embeddings are strings turn them to list of numbers
    embeddings = np.array(df['embeddings'].apply(ast.literal_eval).tolist(), dtype="float32")

    #create faiss index

    diemension = embeddings.shape[1]

    index = faiss.IndexFlatL2(diemension)

    #add vecotrs to index
    index.add(embeddings)

    print("Total vecotrs in index: ", index.ntotal)



    query = "large modular sofa with chaise"
    query_vec = model.encode([query]).astype("float32")

    D,I = index.search(query_vec, k=5)

    for idx, dist in zip(I[0], D[0]):
        print("distance: ", dist)
        print("TExt: ", df.iloc[idx]["chunk_text"])
        print("SKU ", df.iloc[idx]["sku"])
        print("-" * 40)