from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass

class BalanceUpdate(BaseModel):
    amount: float   # can be + or -

class TypeUpdate(BaseModel):
    type: Literal["buyer", "seller", "admin"]

class UserResponse(UserBase):
    type: str
    id: int
    balance: float
    role: str
    status: bool
    created_at: datetime

    class Config:
        from_attributes = True