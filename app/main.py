from fastapi import FastAPI

app = FastAPI(title="beacon-api", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "beacon-api"}

@app.get("/")
def root():
    return {"message": "beacon-api is running", "docs": "/docs"}