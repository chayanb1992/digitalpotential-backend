from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PendingPaymentBase(BaseModel):
    user_id: int
    method_id: int
    network_id: int
    amount: float
    transaction_hash: str
    note: Optional[str] = None

class PendingPaymentCreate(PendingPaymentBase):
    pass

class PendingPaymentUpdate(BaseModel):
    status: str

class PendingPaymentResponse(PendingPaymentBase):
    id: int
    user_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True