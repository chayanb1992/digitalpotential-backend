from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class PaymentAddress(Base):
    __tablename__ = "payment_addresses"

    id = Column(Integer, primary_key=True)
    network_id = Column(Integer, ForeignKey("payment_networks.id"))
    wallet_address = Column(String(255))
    # qr_code = Column(String(255))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    network = relationship("PaymentNetwork", back_populates="addresses")