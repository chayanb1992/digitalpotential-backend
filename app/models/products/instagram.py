from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from ...database import Base


class Instagram(Base):
    __tablename__ = "instagram_accounts"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    email_password = Column(String)
    twofa_code = Column(String)
    sold = Column(Boolean, default=False)

    seller_id = Column(Integer, ForeignKey("users.id"))
    cardInfo_id = Column(Integer, ForeignKey("cardInfos.id"))

    seller = relationship("User", back_populates="instagram_accounts")

    cardInfo = relationship("CardInfo", back_populates="instagram_accounts")