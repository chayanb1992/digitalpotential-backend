from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DepositBase(BaseModel):
    user_id: int
    method_id: int
    network_id: int
    amount: float


class DepositCreate(DepositBase):
    pass


class DepositResponse(DepositBase):
    id: int
    receive_amount: float
    status: str
    tx_hash: Optional[str]
    proof_image: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True