from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
from .products.instagram import Instagram


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    balance = Column(DECIMAL(12,2), default=0)
    role = Column(String(20), default="user")
    type = Column(String(100), default="Buyer")
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    deposits = relationship("Deposit", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
    pending_payments = relationship("PendingPayment", back_populates="user")

    stores = relationship("Store", back_populates="owner")

    # FIXED
    instagram_accounts = relationship("Instagram", back_populates="seller")
    cardInfos = relationship("CardInfo", back_populates="seller")