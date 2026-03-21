from django.core.management.base import BaseCommand
from search.models import ProductEmbedding, ProductData

import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__),"..","..","..",".."))

from transform.embed import create_embeddings
from transform.normalize import normalize_raw_product
from transform.regex_clean import pre_process_regex, post_process_regex, chunk_text
from transform.semantic.semantic_spacy import run_semantic_score
from transform.semantic.semantic_scorer import chunk_and_score
from extract.scrape import scrape_all

from utils.write_semantic_products import write_semantic_products
from utils.utils import save_to_csv

from sentence_transformers import SentenceTransformer


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","..","..","..")
filepath = os.path.join(BASE_DIR, 'etl', 'data', 'scraped_data.csv')

PIPELINE_CONFIG = {
    "semantic_scoring": False,
    "save_debug_csv": True
}


FIELDNAMES_SEMANTIC = [
    "sku",
    "chunk_text",
    "semantic_score",
]

FIELDNAMES_PRODUCT = [
    "sku",
    "name",
    "description",
    "brand",
    "available",
    'currency', 
    "price",
    'updated_at',
    'image',
    'url', 
    'product_raw'
]

model = SentenceTransformer('all-MiniLM-L6-v2')

class Command(BaseCommand):
    help = "Load scraped data in postgres DB"

    def handle(self, *args, **options):

        print("\n === SEMANTIC SEARCH DATA PIPELINE ====\n")

        #normalized data
        products = []

        normalized_products = []

        embedded_products = []

        #scraped data from scraper
        scraped_data = scrape_all()


        for raw in scraped_data:
            print(type(raw))
            normalized = normalize_raw_product(raw)
            if normalized:
                products.append(normalized)

        for product in products:
            product_description = product.product_description
            product_sku = product.product_sku

            product_name = product.product_name
            product_brand = product.product_brand
            product_availability = product.availability

            if not product_description or not product_sku:
                continue

            processed_name = pre_process_regex(product_name)
            processed_description = pre_process_regex(product_description)

            normalized_products.append({
                "sku": product_sku, 
                "name": processed_name, 
                "description": processed_description,
                "brand": product_brand, 
                "available": product_availability,
                "currency":  product.currency,
                "price": product.price,
                "image": product.product_image,
                "url": product.product_url,
                "updated_at": product.updated_at,
                })
            
            embedded_name, embedded_description = create_embeddings(processed_name,processed_description, model)


            embedded_products.append({
            "sku": product_sku,
            "source_type": "name",
            "source_text": processed_name,
            "source_embeddings": embedded_name
            })

            embedded_products.append({
            "sku": product_sku,
            "source_type": "description",
            "source_text": processed_description,
            "source_embeddings": embedded_description
            })



        if PIPELINE_CONFIG["save_debug_csv"]:
            write_semantic_products(filepath, normalized_products, FIELDNAMES_PRODUCT)
        
        if PIPELINE_CONFIG["semantic_scoring"]:
            semantic_scored_results = chunk_and_score()
            write_semantic_products("semantic_products.csv",semantic_scored_results, FIELDNAMES_SEMANTIC)
            

        for product in normalized_products:
            ProductData.objects.get_or_create(
                product_name=product["name"],
                product_sku=product["sku"],
                product_description=product["description"], 
                product_price=product["price"],
                product_image=product["image"],
                product_currency=product["currency"],
                product_url=product["url"],
                product_brand=product["brand"],
                product_is_available=product["available"],
                product_is_active=True,
            )

        # feed embedd data. SKU musst be there
        for product in embedded_products:
            ProductEmbedding.objects.get_or_create(
            embedding_source_type = product["source_type"],
            product_source = ProductData.objects.get(product_sku=product["sku"]) ,
            embedding_source_text = product["source_text"],
            embedding_vector = product["source_embeddings"],
            )
                
   
    

    



