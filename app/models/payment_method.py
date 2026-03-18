from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    slug = Column(String(100), unique=True)
    type = Column(String(50))  # crypto or manual
    icon = Column(String(255))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    networks = relationship("PaymentNetwork", back_populates="method")