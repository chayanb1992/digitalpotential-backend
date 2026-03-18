from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    method_id = Column(Integer, ForeignKey("payment_methods.id"))
    network_id = Column(Integer, ForeignKey("payment_networks.id"))

    amount = Column(DECIMAL(12,2))
    receive_amount = Column(DECIMAL(12,2))
    status = Column(String(50), default="pending")
    tx_hash = Column(String(255))
    proof_image = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="deposits")