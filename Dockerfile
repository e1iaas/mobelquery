FROM python:3.10-slim 
WORKDIR /app/semantic_search_app/
COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt
COPY backend/ .
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "300"]
