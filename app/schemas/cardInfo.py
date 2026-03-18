from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: str
    price: float
    image: Optional[str] = None
    delivery: Optional[str] = None
    star: Optional[float] = 0
    seller_id: int



class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    price: Optional[float]
    image: Optional[str]
    delivery: Optional[str]
    star: Optional[float]


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True