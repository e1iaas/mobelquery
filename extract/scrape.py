import requests
from bs4 import BeautifulSoup
import time
from datetime import date

BASE_URLS = ['https://www.ikea.com/se/en/cat/sofas-fu003/?page={}',
            'https://www.ikea.com/se/en/cat/tables-700675/?page={}',
            'https://www.ikea.com/se/en/cat/chairs-700676/?page={}',
            'https://www.ikea.com/se/en/cat/dining-furniture-700417/?page={}',
            'https://www.ikea.com/se/en/cat/coffee-side-tables-10705/?page={}',
            'https://www.ikea.com/se/en/cat/desks-computer-desks-20649/?page={}',
            'https://www.ikea.com/se/en/cat/desk-chairs-20652/?page={}',
            'https://www.ikea.com/se/en/cat/beds-bm003/?page={}',
            'https://www.ikea.com/se/en/cat/sideboards-buffets-console-tables-30454/?page={}',
            'https://www.ikea.com/se/en/cat/wardrobes-19053/?page={}',
            'https://www.ikea.com/se/en/cat/chests-of-drawers-10451/?page={}',
            'https://www.ikea.com/se/en/cat/hallway-wardrobes-48007/?page={}']

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
results = []

def scrape_page(product_url, page_num):
    formatted_url = product_url.format(page_num)
    response = requests.get(formatted_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = soup.find_all('div', attrs={'data-testid': 'plp-product-card'})

    for e in entries:
        name_el = e.find('span', class_='plp-price-module__product-name')
        description_el = e.find('span', class_='plp-price-module__description')
        price_el = e.find('span', class_='plp-price__sr-text')
        image_el = e.find('img', class_='plp-product__image--alt')
        url_el = e.find('a', class_='plp-product__image-link')
        sku = e['data-product-number']  
        brand = 'IKEA'
        currency = 'SEK'
        updated_at = date.today()

        #Safely extract attrs
        name = name_el.text if name_el else ''
        description = description_el.text if description_el else ''
        price = price_el.text if price_el else ''
        image = image_el['src'] if image_el else ''
        url = url_el ['href'] if url_el else ''

        #only allow data that has this values
        if not name or not price or not image or not url or not sku:
            continue

      

        results.append({
            "name": name, 
            "price": price,
            "image": image,
            "url": url,
            "sku": sku,
            "brand": brand,
            "currency": currency,
            "availability": True,
            "updated_at": updated_at,
            "description": description
            })
    return results


all_results = []

def scrape_all():
    print("scraping all data")
    for url in BASE_URLS:
        page = 1
        time.sleep(2)
        while True:
            results = scrape_page(url,page)
            if not results:
                break
            all_results.extend(results)
            page += 1
    return all_results
       


