import csv

#chunk_id

FIELDNAMES = [
    "sku",
    "chunk_text",
    "semantic_score",
    "category",
    "price_tier",
]


def write_semantic_products(filepath, rows):

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)

