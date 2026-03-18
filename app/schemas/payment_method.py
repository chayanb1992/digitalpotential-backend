from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import List
from .payment_network import PaymentNetworkResponse

class PaymentMethodBase(BaseModel):
    name: str
    slug: str
    type: str
    icon: Optional[str]


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodResponse(PaymentMethodBase):
    id: int
    status: bool
    created_at: datetime
    networks: List[PaymentNetworkResponse] = []

    class Config:
        from_attributes = True