# MobelQuery — AI Furniture Search
A full-stack semantic search application for furniture discovery. Instead of keyword matching, users describe what they're looking for in natural language and the engine returns results based on semantic meaning using cosine similarity over vector embeddings.

Live at [mobelquery.com](https://www.mobelquery.com)

Built by [e1iaas](https://github.com/e1iaas)

---

## Architecture

**Frontend**
- React + Tailwind CSS
- Hosted on Vercel

**Backend**
- Django REST Framework
- PostgreSQL + pgvector for vector storage and similarity search
- Hosted on AWS EC2

**ML Pipeline**
- SpaCy for semantic scoring and text preprocessing
- SentenceTransformer `all-MiniLM-L6-v2` for generating 384-dimensional embeddings
- Cosine similarity search via pgvector

**How it works**
1. Product descriptions are scored for semantic density using SpaCy
2. The highest-scoring text is embedded using `all-MiniLM-L6-v2`
3. Embeddings are stored in PostgreSQL via pgvector
4. User queries are embedded at runtime and matched against stored vectors using cosine similarity
5. Results are ranked by semantic relevance and returned via REST API

---

## Local Setup

### Prerequisites
- Python 3.12
- Node.js 18+
- PostgreSQL with pgvector extension

### Backend

```bash
# Clone repo
git clone https://github.com/e1iaas/semantic_search_app.git
cd semantic_search_app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Fill in your DB credentials in .env

# Run migrations
cd backend
python manage.py migrate

# Load product data
python manage.py load_products
python manage.py load_embeddings

# Start server
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit [http://localhost:5173](http://localhost:5173)

---

## API

### Search endpoint
```
GET /api/?q=<query>&page=<page_number>
```

**Parameters**
- `q` — search query string
- `page` — page number (default: 1)

**Response**
```json
{
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
      "name": "Sophia Modular Sofa",
      "description": "4-piece modular sofa with feather cushions.",
      "url": "https://example.com/product",
      "image": "https://example.com/image.jpg",
      "available": true,
      "price": "1299.00",
      "currency": "USD"
    }
  ]
}
```

---

## Changelog

**2026-03-07**
- Migrated from FAISS to PostgreSQL + pgvector
- Added Django ORM models for products and embeddings
- Replaced in-memory vector search with persistent DB similarity search
- Added Django management commands for data loading

**2026-02-18**
- Added React frontend
- Added pagination to API response

**2026-02-08**
- Added loader.py for separate data and embedding loading
- Added pagination and error handling

**2026-02-03**
- Added Django REST API
- Improved semantic scoring pipeline

**2026-01-16**
- Initial ETL pipeline with semantic search