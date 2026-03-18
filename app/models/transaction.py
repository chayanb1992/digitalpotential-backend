from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    type = Column(String(50))  # deposit / withdraw / purchase
    amount = Column(DECIMAL(12,2))
    balance_before = Column(DECIMAL(12,2))
    balance_after = Column(DECIMAL(12,2))
    reference_id = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")