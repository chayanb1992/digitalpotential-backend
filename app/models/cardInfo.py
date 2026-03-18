from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class CardInfo(Base):
    __tablename__ = "cardInfos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String(255), nullable=True)
    delivery = Column(String(100), nullable=True)
    star = Column(Float, default=0)

    seller_id = Column(Integer, ForeignKey("users.id"))

    seller = relationship("User", back_populates="cardInfos")

    # ✅ FIXED RELATIONSHIP
    instagram_accounts = relationship(
        "Instagram",
        back_populates="cardInfo",
        cascade="all, delete"
    )