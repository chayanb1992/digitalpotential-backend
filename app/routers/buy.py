from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..models.products.instagram import Instagram
from ..models.cardInfo import CardInfo

router = APIRouter(prefix="/buy", tags=["Buy"])

@router.post("/{card_id}")
def buy_accounts(
    card_id: int,
    quantity: int = Query(..., gt=0),
    user_id: int = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    # 1️⃣ Get user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 2️⃣ Get card
    card = db.query(CardInfo).filter(CardInfo.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    total_price = card.price * quantity

    # 3️⃣ Check balance
    if float(user.balance) < total_price:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # 4️⃣ Get available accounts
    accounts = db.query(Instagram).filter(
        Instagram.cardInfo_id == card_id,
        Instagram.sold == False
    ).limit(quantity).all()

    if len(accounts) < quantity:
        raise HTTPException(status_code=400, detail="Not enough accounts available")

    # 5️⃣ Deduct balance
    user.balance = float(user.balance) - total_price

    # 6️⃣ Mark as sold (or delete)
    result_accounts = []

    for acc in accounts:
        acc.sold = True  # ✅ better than delete
        result_accounts.append({
            "username": acc.username,
            "password": acc.password,
            "email": acc.email,
            "email_password": acc.email_password,
            "twofa_code": acc.twofa_code
        })

    db.commit()

    return {
        "message": "Purchase successful",
        "accounts": result_accounts,
        "total_price": total_price
    }