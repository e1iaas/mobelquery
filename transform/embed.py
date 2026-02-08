import pandas as pd
from sentence_transformers import SentenceTransformer

#Embedds DF takes 2 arguments file path and DF-column example: "my_csv_file.csv", "chunk_text" ) 

def create_embeddings_local(csv_file,df_data, output_file):
    print("\n" + "=" * 60)
    print("CREATING EMBEDDINGS (LOCAL)")
    print("=" * 60)

    print(f"\n Loading data from file: {csv_file}...")
    df = pd.read_csv(csv_file)

    print("\n Loading embedding model...")
    print("   Model: all-MiniLM-L6-v2 (384 dimensions)")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded.")

    print(f"\n creating embeddings for {len(df)} products...")
    embeddings = model.encode(
        df[df_data].tolist(),
        show_progress_bar=True,
        batch_size=32,
        convert_to_numpy=True
    )

    print(f"\n Created embeddings!")
    print(f"    Shape: {embeddings.shape}")
    print(f"    Dimensions: {embeddings.shape[1]}")

    df['embeddings'] = embeddings.tolist()

    print(f"\n saving to: {output_file}...")
    df.to_csv(output_file, index=False)
    print(f" Saved {len(df)} products with embeddings")

    print("\n Embedding Stats:")
    print(f"   Vector dimensions: {embeddings.shape[1]}")
    print(f"   Total vectors: {embeddings.shape[0]}")
    print(f"   Memory size: {embeddings.nbytes / 1024 / 1024:.2f} MB")

    print("\n" + "=" * 60)


def analyze_data(df):
    """Quick data analysis"""
    print("=" * 60)
    print(" DATA ANALYSIS")
    print("=" * 60)

    print(f"\n Overview:")
    print(f"  Total products: {len(df)}")
    print(f"  Unique SKUs: {df['sku'].nunique()}")

    print(f"\n Text Length:")
    print(f"  Average: {df['text_length'].mean():.0f} characters")
    print(f"  Min: {df['text_length'].min()}")
    print(f"  Max: {df['text_length'].max()}")

    print(f"\n Top 5 Categories:")
    top_cats = df['category'].value_counts().head(5)
    if len(top_cats) > 0:
        print(top_cats.to_string())
    else:
        print("  No categories found")

    print("\n" + "=" * 60)
