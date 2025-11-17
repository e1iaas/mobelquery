import csv
from dataclasses import  asdict
def save_to_csv(products, filename):

    if not products:
        print("No products to save")
        return

    with open (filename, 'w', newline='', encoding='utf-8') as file:

        fieldnames = ['name', 'description', 'category', 'url', 'price',
                      'currency', 'image', 'availability', 'tracking_url',
                      'sku', 'updated_at']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for product in products:
            writer.writerow(asdict(product))

        print(f" Saved {len(products)} products to {filename}")