print("IMPORTING QUERY")
from search.models import ProductEmbedding
from sentence_transformers import SentenceTransformer
from pgvector.django import CosineDistance
import traceback

model = None

def run_query(query):
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    print("encoding model query")
    try:
        query_vec = model.encode(query).astype("float32")
        embeddings = ProductEmbedding.objects.select_related('product_source').order_by(CosineDistance('embedding_vector', query_vec))[:100]
        results = []
        for e in embeddings:
            product = e.product_source
            results.append({
                "name": e.embedding_source_text if e.embedding_source_type == "name" else product.product_name,
                "description": e.embedding_source_text if e.embedding_source_type == "description" else "",
                "url": product.product_url,
                "image": product.product_image,
                "available": product.product_is_available,
                "price": product.product_price,
                "currency": product.product_currency,
                "brand": product.product_brand
            })
        final_response = {
            "query": query,
            "count": len(results),
            "results": results
        }
        print("return final result: ", final_response)
        return final_response
    except Exception as e:
        traceback.print_exc()
        return {"Error": "internal server error"}
