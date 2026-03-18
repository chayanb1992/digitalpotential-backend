from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import List
from .payment_address import PaymentAddressResponse

class PaymentNetworkBase(BaseModel):
    method_id: int
    network_name: str
    network_slug: str
    fee: float
    min_deposit: float


class PaymentNetworkCreate(PaymentNetworkBase):
    pass


class PaymentNetworkResponse(PaymentNetworkBase):
    id: int
    status: bool
    created_at: datetime
    addresses: List[PaymentAddressResponse] = []

    class Config:
        from_attributes = True