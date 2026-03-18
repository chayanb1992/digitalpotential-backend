from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import cardInfo
from ..models import cardInfo as cardInfoModel

router = APIRouter(
    prefix="/card-info",
    tags=["CardInfo"]
)


@router.get("/", response_model=List[cardInfo.ProductResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(cardInfoModel.CardInfo).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=cardInfo.ProductResponse)
def create_user(new_user: cardInfo.ProductCreate, db: Session = Depends(get_db)):

    existing_user = db.query(cardInfoModel.CardInfo).filter(
        cardInfoModel.CardInfo.title == new_user.title
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_obj = cardInfoModel.CardInfo(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj

@router.get("/{seller_id}", response_model=List[cardInfo.ProductResponse])
def get_user_by_seller_id(seller_id: str, db: Session = Depends(get_db)):
    users = db.query(cardInfoModel.CardInfo).filter(
        cardInfoModel.CardInfo.seller_id == seller_id
    ).all()

    return users

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    account = db.query(cardInfoModel.CardInfo).filter(cardInfoModel.CardInfo.id == id).first()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    db.delete(account)
    db.commit()

    return {"message": "Account deleted"}

@router.get("/single/{id}", response_model=cardInfo.ProductResponse)
def get_card(id: int, db: Session = Depends(get_db)):
    card = db.query(cardInfoModel.CardInfo).filter(
        cardInfoModel.CardInfo.id == id
    ).first()

    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    return card