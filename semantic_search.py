from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np


def semantic_search(query, top_k=5, embedding_file='products_with_embeddings.csv'):
    print(f"\n Searching for: '{query}'")
    print("-" * 60)

    df = pd.read_csv(embedding_file)

    df['embedding_array'] = df['embeddings'].apply(lambda x: np.array(eval(x)))

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]

    product_embeddings = np.vstack(df['embedding_array'].values)
    similarities = cosine_similarity([query_embedding], product_embeddings)[0]

    df['similarity'] = similarities

    results = df.nlargest(top_k, 'similarity')

    print(f"\n Top {top_k} Results:\n")

    for idx, (i, row) in enumerate(results.iterrows(), 1):
        print(f"{idx}. [{row['similarity']:.3f}] {row['name']}")
        print(f"    {row['price']:.2f} {row['currency']} | 📁 {row['category']}")
        print(f"    {row['url'][:60]}...")
        print()

    return results
