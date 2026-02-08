import pandas as pd
import numpy as np
import ast
import faiss
from sentence_transformers import SentenceTransformer 




class Loader:

    def __init__(self):
        self.load()


    def load(self):
        if hasattr(self,"index"):
            return 
        self.load_csv_data()
        self.load_embeddings()


    def load_csv_data(self):

        self.df_stacked_data = pd.read_csv("stacked_product_embeddings.csv")
        self.df_raw_data = pd.read_csv("raw_products.csv")

        
        self.df_raw_index_sku = (
            self.df_raw_data
            .set_index("sku")
            .to_dict(orient="index")
        )
        print("loaded csv")
                

    def load_embeddings(self):
        print("loading model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

        print("converting embeddings... ")
        self.df_stacked_data["source_embeddings"] = self.df_stacked_data["source_embeddings"].apply(
            lambda x: np.array(ast.literal_eval(x), dtype="float32")
        )

        print("stacking embeddings")
        embeddings = np.vstack(self.df_stacked_data["source_embeddings"].values)

        diemension = embeddings.shape[1]

        index = faiss.IndexFlatL2(diemension)
        print("adding embeddings to index")
        index.add(embeddings)

        self.model = model
        self.index = index
        self.faiss_index_to_sku = self.df_stacked_data["sku"].tolist()

        print("loaded sku: ", len(self.df_stacked_data))
        print("faiss vecotrs: ", self.index.ntotal)


