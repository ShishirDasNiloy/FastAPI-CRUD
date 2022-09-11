from typing import List
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import UserUpdate, UserIn, UserOut
from repositories import roles_repo
from database import get_db
from sqlalchemy.orm import Session
from services import roles_service

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def read(db: Session = Depends(get_db)):
    roles= roles_service.get(database=db)
    return handle_result(roles)

@router.post("/")
def create( data_in: UserIn, db: Session = Depends(get_db)):
    role = roles_service.create(data_in=data_in, database=db)
    return handle_result(role)

@router.get("/{id}", response_model=UserOut)
def read_with_id(id: int, db: Session = Depends(get_db)):
    roles = roles_service.get_one(database=db, id=id)
    return handle_result(roles)

@router.patch("/{id}", response_model=UserOut)
def update_all(data_update: UserUpdate, id: int, db: Session = Depends(get_db)):
    update = roles_service.update(database=db, id=id, data_update=data_update)
    return handle_result(update)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    delete = roles_service.delete(database=db, id=id)
    return handle_result(delete)
