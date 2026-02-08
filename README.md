# Semantic Search App

A full-stack web application that provides semantic search over product data using sentence embeddings and FAISS. Users can query for Furniture products, and the API returns relevant results with name, description, and URL.

by e1iaaas


# Installation

1. clone repo

git clone https://github.com/e1iaas/semantic_search_app.git
cd semantic_search_app

2. Create enviorment

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Install dependencies

pip install -r requirements.txt

4. Run server

cd backend
python manage.py runserver

5. Query for response

http://127.0.0.1:8001/api/?q="query"&page=1

?q= " your query " string
&page= "optional page number " int




## Response Format

The API returns JSON with the following fields:

- `query` → The search query string
- `count` → Total number of results
- `page` → Current page number
- `page_size` → Number of results per page
- `results` → Array of result objects

Each result object contains:

- `name` → Product name (can be null)
- `description` → Product description
- `url` → Product URL

Example:
```json
{
    "query": "modular sofa",
    "count": 2,
    "page": 1,
    "page_size": 5,
    "results": [
        {
            "name": "Sophia Modular Sofa",
            "description": "2-piece modular sofa.",
            "url": "https://chitaliving.com/products/sophia-2-piece-feather-modular-sofa"
        },
        {
            "name": "Liam Modular Sofa",
            "description": "2-piece oversized modular sofa.",
            "url": "https://chitaliving.com/products/liam-2-piece-overstuffed-feather-wood-base-sectional"
        }
    ]
}






END GOAL: 

-full working etl pipeline that fetches data 
from furnitur apis embeds semantic products descriptions
pipe to simple CRUD SITE

-end user searches for furniture returns results
similar in semantic meaning in a doom scroll content like way







CURRENT UPDATE - 2026 - 02 -08
-added loader.py handles loading of data and embeddings seperately
-added pagination to api endpoint and simple error handling
-updated README 

UDPATE - 2026 - 02 - 03
-added simple api for testing with DJANGO
-tweaked the seamntic scoring filter, added colors (pos == ADJ) for more accurate scoring
-pipline only return #1 semantic description from product descriptions to embedd

UPDATE - 2026 - 01 - 16
simple pipeline built fetches TEST data from a csv 
-normalizes the data, 
-chunks product description 
-scores chunks for semantic meaning returns highest score



