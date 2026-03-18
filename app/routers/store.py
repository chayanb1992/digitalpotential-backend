from fastapi import HTTPException, status, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import store
from ..models import store as storeModel

router = APIRouter(
    prefix="/stores",
    tags=["Store"]
)


@router.get("/", response_model=List[store.StoreResponse])
def get_stores(db: Session = Depends(get_db)):
    stores = db.query(storeModel.Store).all()
    return stores


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=store.StoreResponse)
def create_store(new_store: store.StoreCreate, db: Session = Depends(get_db)):

    existing_store = db.query(storeModel.Store).filter(
        storeModel.Store.store_name == new_store.store_name
    ).first()

    if existing_store:
        raise HTTPException(
            status_code=400,
            detail="This store already exists"
        )

    store_obj = storeModel.Store(**new_store.model_dump())
    # store_obj = storeModel.Store(**new_store.model_dump(), owner_id=current_user.id)

    db.add(store_obj)
    db.commit()
    db.refresh(store_obj)

    return store_obj


@router.get("/{owner_id}", response_model=store.StoreResponse)
def get_store_by_name(owner_id: str, db: Session = Depends(get_db)):

    store = db.query(storeModel.Store).filter(
        storeModel.Store.owner_id == owner_id
    ).first()

    if not store:
        raise HTTPException(
            status_code=404,
            detail="Store not found"
        )

    return store