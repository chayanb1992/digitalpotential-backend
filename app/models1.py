# from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text, Boolean
# from .databale import Base

# class Accounts(Base):
#     __tablename__ = "all_accounts_info"

#     id = Column(Integer, primary_key=True)
#     username = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     email_password = Column(String, nullable=False)
#     creator_email = Column(String, nullable=False)
#     title = Column(String, nullable=False)
#     platform = Column(String, nullable=False)
#     age = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     followers = Column(String, nullable=False)
#     price = Column(String, nullable=False)

# class User(Base):
#     __tablename__ = "all_users_info"
#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     user_catagory = Column(String, nullable=False)
#     balance = Column(String, nullable=False, server_default="0.0")
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# class Wallat(Base):
#     __tablename__ = "wallet"
#     id = Column(Integer, primary_key=True, nullable=False)
#     owener_email = Column(String, nullable=False, unique=True)
#     current_ballance = Column(String, nullable=False)

# class Catalog(Base):
#     __tablename__ = "catalogs"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, unique=True, index=True)
#     products = Column(Integer, nullable=False)
#     image = Column(String, nullable=False)
#     isNew = Column(Boolean, default=False)

