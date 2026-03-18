from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class StoreBase(BaseModel):
    store_name: str
    owner_id: int
    description: str
    rules: str
    telegram: str

class StoreCreate(StoreBase):
    logo: str

class StoreResponse(StoreBase):
    id: int
    logo: str
    status: str
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True