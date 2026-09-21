from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=True)
    category = Column(String, nullable=False)  # deployed-apps | infrastructure | portfolio
    status = Column(String, nullable=False)    # running | deploying | planned | docs
    label = Column(String, nullable=False)     # RUNNING | JOINING | ...
    created_at = Column(DateTime, default=datetime.utcnow)