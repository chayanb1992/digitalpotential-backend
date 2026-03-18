from fastapi import FastAPI, HTTPException, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models1, schema
from sqlalchemy.orm import Session
from .database import engine, get_db
from typing import List

app = FastAPI()
models1.Base.metadata.create_all(bind=engine)




while True:
    try:
        conn = psycopg2.connect(host='localhost', database="postgres", user="postgres", password="1234", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successfully connect Database")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error:" , error)
        time.sleep(3)


@app.get("/", response_model=List[schema.AccountResponse])
def read_root(db: Session = Depends(get_db)):
    accounts = db.query(models1.Account).all()
    return accounts


@app.post('/account', response_model=schema.AccountResponse)
def create_account(account:schema.Account, db: Session = Depends(get_db)):
    new_account = models1.Account(**account.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account



@app.get("/user/{id}", response_model=schema.AccountResponse)
def get_account(id: int, db:Session = Depends(get_db)):
    account = db.query(models1.Account).filter(models1.Account.id == id).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account with id:{id} was not found"
        )

    return account

@app.get("/users", status_code=status.HTTP_201_CREATED)
def account_user(user:schema.UserCreate, db:Session=Depends(get_db)):
    new_user = models1.User

@app.get("/accountsalchemy")
def account(db: Session = Depends(get_db)):
    return {"status": "sqlalchemy orm working"}