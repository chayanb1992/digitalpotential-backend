from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import user
from ..models import user as userModel

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[user.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(userModel.User).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user.UserResponse)
def create_user(new_user: user.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(userModel.User).filter(
        userModel.User.email == new_user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_obj = userModel.User(**new_user.model_dump())

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj

@router.get("/{email}", response_model=user.UserResponse)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.email == email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.patch("/balance/{user_id}", response_model=user.UserResponse)
def update_balance(
    user_id: int,
    payload: user.BalanceUpdate,
    db: Session = Depends(get_db)
):
    user_obj = db.query(userModel.User).filter(
        userModel.User.id == user_id
    ).first()

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert DECIMAL → float safely
    current_balance = float(user_obj.balance or 0)

    new_balance = current_balance + payload.amount

    # Prevent negative balance
    if new_balance < 0:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    user_obj.balance = new_balance

    db.commit()
    db.refresh(user_obj)

    return user_obj

@router.patch("/become-seller/{user_id}", response_model=user.UserResponse)
def become_seller(user_id: int, db: Session = Depends(get_db)):
    user_obj = db.query(userModel.User).filter(
        userModel.User.id == user_id
    ).first()

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    if user_obj.type == "seller":
        raise HTTPException(status_code=400, detail="Already a seller")

    user_obj.type = "seller"

    db.commit()
    db.refresh(user_obj)

    return user_obj