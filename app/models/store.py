from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)

    store_name = Column(String(150), unique=True, nullable=False)
    description = Column(Text)
    rules = Column(Text)

    telegram = Column(String(100))
    logo = Column(String(255))

    status = Column(String(20), default="pending")

    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="stores")