from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import payment_address
from ..models import payment_address as paymentaddress

router = APIRouter(
    prefix="/paymentaddress",
    tags=["Payment_address"]
)

@router.get("/", response_model=List[payment_address.PaymentAddressResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(paymentaddress.PaymentAddress).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=payment_address.PaymentAddressResponse)
def create_user(new_user: payment_address.PaymentAddressCreate, db: Session = Depends(get_db)):

    existing_user = db.query(paymentaddress.PaymentAddress).filter(
        paymentaddress.PaymentAddress.wallet_address == new_user.wallet_address
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Wallet address already exists"
        )

    user_obj = paymentaddress.PaymentAddress(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj