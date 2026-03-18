from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    method = Column(String(100))
    wallet_address = Column(String(255))
    amount = Column(DECIMAL(12,2))
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)