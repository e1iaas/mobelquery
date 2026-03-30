MobelQuery — AI Furniture Search
A full-stack semantic search engine for furniture discovery. Users describe what they're looking for in natural language and the engine returns results based on semantic meaning using cosine similarity over vector embeddings.
Live at mobelquery.com

Architecture
Frontend

React + Tailwind CSS
Hosted on Vercel

Backend

Django REST Framework
PostgreSQL + pgvector for vector storage and similarity search
Hosted on AWS EC2
Automated deployment via GitHub Actions

ML / Search

SentenceTransformer all-MiniLM-L6-v2 for generating 384-dimensional embeddings
Cosine similarity search via pgvector


Data Pipeline
Product data is scraped from IKEA across 12 furniture categories using BeautifulSoup. Each product goes through a normalize → embed → load sequence before being stored in PostgreSQL.
A cron job runs the full pipeline nightly on EC2 to keep data fresh.
scrape → normalize → generate embeddings → load into PostgreSQL
The pipeline is triggered via a Django management command:
bashpython manage.py run_pipeline

How Search Works

Product names and descriptions are embedded using all-MiniLM-L6-v2
Embeddings are stored in PostgreSQL via pgvector
At query time, the user's input is embedded and matched against stored vectors using cosine similarity
Results are ranked by semantic relevance and returned via the REST API


Local Setup
Prerequisites

Python 3.10+
Node.js 18+
PostgreSQL with pgvector extension

Backend
bashgit clone https://github.com/e1iaas/semantic_search_app.git
cd semantic_search_app

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Fill in your DB credentials in .env

cd backend
python manage.py migrate
python manage.py run_pipeline

python manage.py runserver
Frontend
bashcd frontend
npm install
npm run dev
```

Visit [http://localhost:5173](http://localhost:5173)

---

## API

### Search endpoint
```
GET /api/?q=<query>&page=<page_number>
Parameters

q — natural language search query
page — page number (default: 1)

Response
json{
  "query": "cozy modular sofa",
  "count": 100,
  "page_obj": {
    "page_number": 1,
    "page_size": 12,
    "has_next": true,
    "has_prev": false
  },
  "results": [
    {
      "name": "VIMLE",
      "description": "3-seat sofa, Gunnared beige",
      "url": "https://www.ikea.com/se/en/p/...",
      "image": "https://www.ikea.com/...",
      "available": true,
      "price": 5995,
      "currency": "SEK",
      "brand": "IKEA"
    }
  ]
}
```

---

## CI/CD

Pushing to `master` triggers a GitHub Actions workflow that SSHs into EC2 and runs:
```
git pull → pip install → migrate → restart gunicorn