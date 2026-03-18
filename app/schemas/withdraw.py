from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WithdrawalBase(BaseModel):
    user_id: int
    method: str
    wallet_address: str
    amount: float


class WithdrawalCreate(WithdrawalBase):
    pass


class WithdrawalResponse(WithdrawalBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True