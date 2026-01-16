#normalize data after fetch

from dataclasses import dataclass

@dataclass
class NormalizedProduct:
    product_category: str  #CATEGORY desk, chair, table
    product_name: str #name of furniture
    product_brand: str
    price_tier: str # budget, mid, high, premium, luxury
    availability: bool #in stock | not in stock
    currency: str #euro | usd etc
    product_image: str
    product_url: str
    product_sku: str
    updated_at: int
    product_raw: dict

CATEGORY_MAPPING = {
    "sofa": ["sofa", "couch", "sectional", "loveseat", "ottoman"],
    "bed": ["bed", "mattress", "headboard"],
    "table": ["table", "desk", "dining table"],
    "chair": ["chair", "stool", "armchair", "recliner"],
    "storage": ["shelf", "cabinet", "wardrobe", "dresser"],
}

REJECT_KEYWORDS = [
    "warranty",
    "insurance",
    "replacement plan",
    "protection",
    "assembly service",
    "seel"
]

PRICE_RULES = [
    ("budget", 50),
    ("mid", 150),
    ("high", 300),
    ("premium", 600),
    ("luxury", float("inf"))
]


def map_category(raw_category: str) -> str | None:
    #if not category reject
    if not raw_category:
        return None

    #normilize  raw category data to lowercase
    #FIX also remove & and -
    text = raw_category.lower().rstrip("s")

    #if category is in reject_keyword reject
    for keyword in REJECT_KEYWORDS:
        if keyword in text:
            return None

    #if category map it
    for category, keywords in CATEGORY_MAPPING.items():
        for keyword in keywords:
            if keyword in text:
                return category

    #unkown category reject
    return None

def normalize_price(raw_price: float | int) -> str | None:
    if not raw_price or raw_price == "":
        return None

    raw_price = float(raw_price)

    for tier_name, max_price in PRICE_RULES:
        if raw_price <= max_price:
            return tier_name




#THEN TRANSFORM FUNCTION
def normalize_raw_product(raw_product):

    raw_dict = raw_product

    normalized_category = map_category(raw_product.get("category"))
    if normalized_category is None:
        return None

    normalized_price_tier = normalize_price(raw_product.get("price", 0))
    if normalized_price_tier is None:
        return None

    raw_availability = raw_product.get("availability", "N/A")
    normalized_availability = bool(raw_availability)

    raw_currency = raw_product.get("currency", "USD")
    normalized_currency = raw_currency.upper()

    normalized_product = NormalizedProduct(
        product_category = normalized_category,
        product_name = raw_product.get("name"),
        product_brand = raw_product.get("brand"),
        price_tier = normalized_price_tier,
        availability =  normalized_availability,
        currency = normalized_currency,
        product_image = raw_product.get("image"),
        product_url = raw_product.get("url"),
        product_sku = raw_product.get("sku"),
        updated_at = raw_product.get("updated_at"),
        product_raw = raw_dict
    )

    return normalized_product
