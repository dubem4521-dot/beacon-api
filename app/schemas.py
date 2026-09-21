from datetime import datetime
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    url: str | None = None
    category: str
    status: str = "running"
    label: str = "RUNNING"


class ItemOut(BaseModel):
    id: int
    name: str
    url: str | None
    category: str
    status: str
    label: str
    created_at: datetime

    class Config:
        from_attributes = True