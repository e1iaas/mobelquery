import csv

fieldnames = [
    "name","description","category","url","price","currency","image","availability","long_url","sku","updated_at"

]

def load_from_csv(path):
    with open(path, newline = "", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames = fieldnames)
        products = list(reader)

        if products:
            print(f"CSV Columns: {products[0].keys()}")

        return products