import requests
from dataclasses import dataclass, asdict
import time

@dataclass
class Product:
    name: str
    description: str
    category: str
    url: str
    price: float
    currency: str
    image: str
    availability: bool
    tracking_url: str
    sku: str
    updated_at: int



def fetch_products(url, base_param):
    all_products = []
    page = 1


    while True:
        params = base_param.copy()
        params['page'] = page

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()

            status = data.get('status', {})
            if status.get('code') !=0:
                print(f"API Error: {status.get('msg')}")
                break

            api_data = data.get('data', {})
            results = api_data.get('list', [])

            if not results:
                break

            for item in results:
                product = Product(
                    name=item.get('name', ''),
                    description=item.get('description', ''),
                    category=item.get('category', ''),
                    url=item.get('url', ''),
                    tracking_url=item.get('tracking_url_short', ''),
                    price=float(item.get('price', 0)),
                    currency=item.get('currency', ''),
                    image=item.get('image', ''),
                    availability=item.get('availability', '') == 'in stock',
                    sku=item.get('sku', ''),
                    updated_at=int(item.get('updated_at', 0))
                )
                all_products.append(product)

            print(f"Page {page}: {len(results)} products ({len(all_products)} total)")

            page += 1
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"Error on page {page}: {e}")
            break


    return all_products





