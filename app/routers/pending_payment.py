from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import pending_payment
from ..models import pending_payment as paymentPayment

router = APIRouter(
    prefix="/payments",
    tags=["Pending Payments"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=pending_payment.PendingPaymentResponse)
def create_user(new_user: pending_payment.PendingPaymentCreate, db: Session = Depends(get_db)):

    existing_user = db.query(paymentPayment.PendingPayment).filter(
        paymentPayment.PendingPayment.transaction_hash == new_user.transaction_hash
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="This transaction already exists"
        )

    user_obj = paymentPayment.PendingPayment(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj