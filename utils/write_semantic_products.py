import csv

#chunk_id

def write_semantic_products(filepath, rows, FIELDNAMES):

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)

