# from fastapi import HTTPException, status, Depends, APIRouter
# from typing import List
# from sqlalchemy.orm import Session
# from .. import models1, schema
# from ..databale import get_db

# router = APIRouter()

# @router.get("/accounts", response_model=List[schema.AccountResponse])
# def read_root(db: Session = Depends(get_db)):
#     accounts = db.query(models1.Accounts).all()
#     return accounts

# @router.post('/addaccount', response_model=schema.AccountResponse)
# def create_account(account:schema.Account, db: Session = Depends(get_db)):
#     new_account = models1.Accounts(**account.model_dump())
#     db.add(new_account)
#     db.commit()
#     db.refresh(new_account)
#     return new_account

# # @app.post("/post")
# # def create_post(post: schema.Account):
# #     cursor.execute("""
# #     INSERT INTO accounts(username, password, email, email_password)
# #     VALUES (%s, %s, %s, %s)
# #     RETURNING *
# #     """, (post.username, post.password, post.email, post.email_password))

# #     new_post = cursor.fetchone()
# #     conn.commit()
# #     return {"Data": new_post}

# # @router.post('/account', response_model=schema.AccountResponse)
# # def create_account(account:schema.Account, db: Session = Depends(get_db)):
# #     new_account = models.Account(**account.model_dump())
# #     db.add(new_account)
# #     db.commit()
# #     db.refresh(new_account)
# #     return new_account


# # @app.get("/user/{id}")
# # def get_user(id: int):
# #     cursor.execute("SELECT * FROM accounts WHERE id = %s", (id,))
# #     user = cursor.fetchone()

# #     if user is None:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail=f"Account with id:{id} was not found"
# #         )

# #     return {"Accounts_details": user}

# # @router.get("/user/{id}", response_model=schema.AccountResponse)
# # def get_account(id: int, db:Session = Depends(get_db)):
# #     account = db.query(models.Account).filter(models.Account.id == id).first()
# #     if not account:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail=f"Account with id:{id} was not found"
# #         )

# #     return account
