from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import payment_method
from ..models import payment_method as paymentMethod

router = APIRouter(
    prefix="/paymentmethod",
    tags=["Payment_method"]
)

@router.get("/", response_model=List[payment_method.PaymentMethodResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(paymentMethod.PaymentMethod).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=payment_method.PaymentMethodResponse)
def create_user(new_user: payment_method.PaymentMethodCreate, db: Session = Depends(get_db)):

    existing_user = db.query(paymentMethod.PaymentMethod).filter(
        paymentMethod.PaymentMethod.name == new_user.name
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Methos already exists"
        )

    user_obj = paymentMethod.PaymentMethod(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj