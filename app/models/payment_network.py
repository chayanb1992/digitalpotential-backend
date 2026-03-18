from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class PaymentNetwork(Base):
    __tablename__ = "payment_networks"

    id = Column(Integer, primary_key=True)
    method_id = Column(Integer, ForeignKey("payment_methods.id"))
    network_name = Column(String(100))
    network_slug = Column(String(100))
    fee = Column(DECIMAL(10,2), default=0)
    min_deposit = Column(DECIMAL(10,2))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    method = relationship("PaymentMethod", back_populates="networks")
    addresses = relationship("PaymentAddress", back_populates="network")