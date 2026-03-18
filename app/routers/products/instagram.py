from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ...database import get_db
from ...schemas.products import instagram
from ...models.products import instagram as productsModel

router = APIRouter(
    prefix="/instagram",
    tags=["Instagram"]
)


@router.get("/", response_model=List[instagram.ProductResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(productsModel.Instagram).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=instagram.ProductResponse)
def create_user(new_user: instagram.ProductCreate, db: Session = Depends(get_db)):

    existing_user = db.query(productsModel.Instagram).filter(
        productsModel.Instagram.username == new_user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_obj = productsModel.Instagram(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj

@router.get("/{cardInfo_id}", response_model=List[instagram.ProductResponse])
def get_user_by_seller_id(cardInfo_id: str, db: Session = Depends(get_db)):
    users = db.query(productsModel.Instagram)\
              .filter(productsModel.Instagram.cardInfo_id == cardInfo_id)\
              .all()

    if not users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    account = db.query(productsModel.Instagram).filter(productsModel.Instagram.id == id).first()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    db.delete(account)
    db.commit()

    return {"message": "Account deleted"}