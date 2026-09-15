# beacon-api

REST API for the Beacon homelab dashboard.

## Stack
- Python 3.12
- FastAPI
- PostgreSQL (phase 2b)

## Run locally

    pip install -r requirements.txt
    uvicorn app.main:app --reload

Then open http://localhost:8000/docs for interactive API docs.

## Run with Docker

    docker build -t rustytoothpickk/beacon-api:latest .
    docker run -d --name beacon-api -p 8000:8000 rustytoothpickk/beacon-api:latest
