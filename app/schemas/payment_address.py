from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentAddressBase(BaseModel):
    network_id: int
    wallet_address: str
    # qr_code: Optional[str]


class PaymentAddressCreate(PaymentAddressBase):
    pass


class PaymentAddressResponse(PaymentAddressBase):
    id: int
    status: bool
    created_at: datetime

    class Config:
        from_attributes = True