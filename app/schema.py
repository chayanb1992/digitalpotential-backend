# from pydantic import BaseModel, HttpUrl, EmailStr
# from datetime import datetime

# #define request body schema
# class Account(BaseModel):
#     username: str
#     password: str
#     email: str
#     email_password: str
#     creator_email: str
#     account_title: str
#     account_age_type: str
#     account_description: str
#     account_follower: str
#     account_price: str

# class AccountResponse(BaseModel):
#     id: int
#     email: str
#     account_title: str
#     account_age_type: str
#     account_description: str
#     account_follower: str
#     account_price: str
#     class Config:
#         orm_model = True
# #catalog add schema
# class Catalog(BaseModel):
#     name: str
#     products: int
#     image: str
#     isNew: bool


# class CatalogResponse(BaseModel):
#     id: int
#     name: str
#     products: int
#     image: str
#     isNew: bool

#     class Config:
#         orm_mode = True

# class UserCreate(BaseModel):
#     email: EmailStr
#     user_catagory: str

# class UserRes(BaseModel):
#     email: EmailStr
#     user_catagory: str
#     balance: str
#     created_at: datetime
#     class Config:
#         orm_model = True

# class LoginUser(BaseModel):
#     email: EmailStr
#     password: str