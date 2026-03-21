from dataclasses import dataclass
import re

@dataclass
class NormalizedProduct:
    product_name: str #name of furniture
    product_brand: str
    product_description: str
    availability: bool #in stock | not in stock
    currency: str #euro | usd etc
    price: float
    product_image: str
    product_url: str
    product_sku: str
    updated_at: int
    
def normalize_raw_product(raw_product):
    print("normalized_product type: ", type(raw_product))

    raw_availability = raw_product.get("availability", "N/A")
    normalized_availability = bool(raw_availability)

    raw_currency = raw_product.get("currency", "")
    normalized_currency = raw_currency.upper()

    raw_price = raw_product.get("price","")
    filterd_price = re.sub(r'[^\d]', '', raw_price)
    normalized_price = float(filterd_price)

    normalized_product = NormalizedProduct(
        product_name = raw_product.get("name"),
        product_brand = raw_product.get("brand"),
        availability =  normalized_availability,
        currency = normalized_currency,
        price = normalized_price,
        product_image = raw_product.get("image"),
        product_url = raw_product.get("url"),
        product_sku = raw_product.get("sku"),
        updated_at = raw_product.get("updated_at"),
        product_description = raw_product.get("description")
    )

    return normalized_product
