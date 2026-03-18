from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import catagory
from ..models import catagory as categoryModels


router = APIRouter(
    prefix="/category",
    tags=["Category"]
)
# get all catalog
@router.get("/", response_model=List[catagory.CategoryResponse])
def read_root(db: Session = Depends(get_db)):
    category = db.query(categoryModels.Category).all()
    return category

# add catalog
@router.post("/", response_model=catagory.CategoryResponse)
def create_category(account: catagory.CategoryCreate, db: Session = Depends(get_db)):
    new_category = categoryModels.Category(**account.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category