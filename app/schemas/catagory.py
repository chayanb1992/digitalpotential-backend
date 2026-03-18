from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    products: int
    image: str
    isNew: bool


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    class Config:
        from_attributes = True