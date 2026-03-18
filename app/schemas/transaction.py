from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    user_id: int
    type: str
    amount: float
    description: Optional[str]


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int
    balance_before: float
    balance_after: float
    reference_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True