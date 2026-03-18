# from fastapi import HTTPException, status, Depends, APIRouter
# from .. import models1, schema
# from sqlalchemy.orm import Session
# from ..databale import engine, get_db
# from ..utility import verify_password
# from ..oatth2 import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
# from datetime import timedelta


# router = APIRouter(tags=["Authentication"])

# @router.post("/login")
# def login(user_credintials:schema.LoginUser, db:Session=Depends(get_db)):
#     user = db.query(models1.User).filter(models1.User.email == user_credintials.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credintial")
#     if not verify_password(user_credintials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credintial")
#     access_token = create_access_token(
#         data = {"user_id": user.id},
#         expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )
#     return {'token': access_token}