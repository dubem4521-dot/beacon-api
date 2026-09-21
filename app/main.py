from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from . import models
from .schemas import ItemCreate, ItemOut

app = FastAPI(title="beacon-api", version="0.1.0")

# Create tables on startup (fine for now; migrations later)
Base.metadata.create_all(bind=engine)

# Dependency: provides a DB session per request, closes it after
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok", "service": "beacon-api"}

@app.get("/")
def root():
    return {"message": "beacon-api is running", "docs": "/docs"}



# ---------- Items ----------
@app.get("/items", response_model=list[ItemOut])
def list_items(category: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Item)
    if category:
        query = query.filter(models.Item.category == category)
    return query.order_by(models.Item.id).all()


@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = models.Item(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return None