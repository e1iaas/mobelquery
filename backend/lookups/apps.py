from django.apps import AppConfig
import csv
import pandas as pd
import numpy as np
import ast
import faiss
from sentence_transformers import SentenceTransformer 




class LookupsConfig(AppConfig):
    name = 'lookups'


    def ready(self):
        if hasattr(self,"index"):
            return 
        self.load_csv_data()
        self.load_embeddings()


    def load_csv_data(self):

        self.df_embedding_data = pd.read_csv("product_embeddings.csv")
        df_raw_data = pd.read_csv("raw_products.csv")

        
        self.df_raw_index_sku = (
            df_raw_data
            .set_index("sku")
            .to_dict(orient="index")
        )
        
                

    def load_embeddings(self):
        model = SentenceTransformer("all-MiniLM-L6-v2")

        embeddings = np.array(self.df_embedding_data["embeddings"].apply(ast.literal_eval).tolist(), dtype="float32")

        diemension = embeddings.shape[1]

        index = faiss.IndexFlatL2(diemension)

        #add vecotrs to index
        index.add(embeddings)

        self.model = model
        self.index = index
        self.faiss_index_to_sku = self.df_embedding_data["sku"].tolist()

        print("loaded sku: ", len(self.df_embedding_data))
        print("faiss vecotrs: ", self.index.ntotal)


