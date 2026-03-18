from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import payment_network
from ..models import payment_network as paymentNetwork

router = APIRouter(
    prefix="/paymentnetwork",
    tags=["Payment_network"]
)

@router.get("/", response_model=List[payment_network.PaymentNetworkResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(paymentNetwork.PaymentNetwork).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=payment_network.PaymentNetworkResponse)
def create_user(new_user: payment_network.PaymentNetworkCreate, db: Session = Depends(get_db)):

    existing_user = db.query(paymentNetwork.PaymentNetwork).filter(
        paymentNetwork.PaymentNetwork.network_name == new_user.network_name
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Network already exists"
        )

    user_obj = paymentNetwork.PaymentNetwork(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj