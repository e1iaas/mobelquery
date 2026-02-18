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

5. Setup frontend

cd frontend

# Install Node.js (version 18+ recommended)

# Download from https://nodejs.org or install via your OS package manager.

brew install node   #macOS with HomeBrew

sudo apt update.  #ubuntu / debian  
sudo apt install nodejs npm -y

winget install OpenJS.NodeJS   #Windows (PowerShell with winget)


# Verify installation:
node -v
npm -v

# Install frontend dependencies
npm install

# Start development server
npm run dev


6. Using api 
go to the localhost link  http://localhost:5173/
query for furniture and return results 





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

Optional fields may be null if data is unavailable:

- `available` → boolean indicating stock availability
- `image` → product image URL
- `price` → numeric price value
- `currency` → ISO currency code


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
            "url": "https://chitaliving.com/products/sophia-2-piece-feather-modular-sofa",
            "available": true,
            "image": "https://example.com/image.jpg",
            "price": 1299.99,
            "currency": "USD"
        },
        {
            "name": "Liam Modular Sofa",
            "description": "2-piece oversized modular sofa.",
            "url": "https://chitaliving.com/products/liam-2-piece-overstuffed-feather-wood-base-sectional",
            "available": false,
            "image": null,
            "price": null,
            "currency": null
        }
    ]
}







END GOAL: 

-full working etl pipeline that fetches data 
from furnitur apis embeds semantic products descriptions
pipe to simple CRUD SITE

-end user searches for furniture returns results
similar in semantic meaning in a doom scroll content like way





UPDATE - 2026 - 02 - 18
-added REACT frontend for the application
-added extra data to api response


UPDATE - 2026 - 02 - 08
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



