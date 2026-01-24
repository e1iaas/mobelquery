import pandas as pd
from datetime import datetime
from filter import regex_clean


def create_embedding_text(row) -> str:
    parts = []

    if row['name']:
        parts.append(f"Product: {row['name']}")

    if row['category']:
        parts.append(f"Category: {row['category']}")

    if row['description']:
        parts.append(f"Description: {row['description']}")

    parts.append(f"Price Category: {row['price_category']}")

    return ". ".join(parts)

def prepare_for_embeddings(products):
    print("Preparing data for embeddings...")

    df = pd.DataFrame([vars(p) for p in products])
    print(f" Starting with {len(df)} products")

    df = df[
        (df['name'].str.len() > 3) &
        (df['price'] > 0) &
        (df['url'].notna()) &
        (df['url'].str.len() > 0) &
        (df['sku'].notna()) &
        (df['availability'] == True)
    ]

    print(f" After quality filters: {len(df)} products")

    df = df.drop_duplicates(subset=['sku'], keep='first')
    print(f"  After removing duplicates: {len(df)} products")

    # === clean text ===
    df['name'] = df['name'].apply(regex_clean)
    df['description'] = df['description'].apply(regex_clean)
    df['category'] = df['category'].apply(regex_clean)

    # --- Price category ---
    labels = ['budget', 'mid-range', 'premium', 'luxury']
    df['price_category'] = pd.qcut(df['price'], q=4, labels=labels, duplicates='drop')

    # --- Embedding text ---
    df['combined_text'] = df.apply(create_embedding_text, axis=1)

    # ===== ADD USEFUL COLUMNS =====
    df['text_length'] = df['combined_text'].str.len()
    df['processed_at'] = datetime.now().isoformat()
    df = df[df['text_length'] >= 20]

    print(f"  Final dataset: {len(df)} products")

    output_df = df[[
        'sku',
        'combined_text',
        'name',
        'description',
        'category',
        'price',
        'currency',
        'price_category',
        'availability',
        'url',
        'tracking_url',
        'text_length',
        'processed_at'
    ]].copy()

    print(f"✓ Data ready for embeddings\n")

    return output_df