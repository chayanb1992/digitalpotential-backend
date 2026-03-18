from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class PendingPayment(Base):
    __tablename__ = "pending_payments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    method_id = Column(Integer, ForeignKey("payment_methods.id"))
    network_id = Column(Integer, ForeignKey("payment_networks.id"))

    amount = Column(Float, nullable=False)

    transaction_hash = Column(String, nullable=True)
    # screenshot = Column(String, nullable=True)
    note = Column(String, nullable=True)

    status = Column(String, default="pending")  # pending / approved / rejected

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="pending_payments")
    method = relationship("PaymentMethod")
    network = relationship("PaymentNetwork")