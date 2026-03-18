from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]
    email_password: Optional[str]
    twofa_code: Optional[str]
    sold: bool
    seller_id: int
    cardInfo_id: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True