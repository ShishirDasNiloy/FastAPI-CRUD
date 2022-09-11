from asyncio import base_tasks
from typing import Generic, Type, TypeVar
from sqlalchemy.orm import Session
from fastapi import status
from database import Base
from pydantic import BaseModel
from repositories import BaseRepo
from exceptions import AppException, ServiceResult

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)
ModelRepo = TypeVar("ModelRepo", bound=BaseRepo)

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType], repo: Type[ModelRepo]):
        self.model = model
        self.repo = repo

    def create(self, database: Session, data_in: CreateSchemaType):
        data = self.repo.create(database, data_in)
        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def get(self,database: Session):
        data=self.repo.get(database)
        if not data:
            data =[]
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def get_one(self,database: Session, id: int):
        data=self.repo.get(database, id)
        if not data:
            return ServiceResult(AppException.NotFound(f"No {self.model.__name__.lower}s found."))
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def update(self, database: Session, id: int, data_update: UpdateSchemaType):
        data = self.repo.update(database, id, data_update)
        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)

    def delete(self, database: Session, id: int):
        remove = self.repo.delete(database, id)
        if remove:
            return ServiceResult("Deleted", status_code=status.HTTP_202_ACCEPTED)
        return ServiceResult(AppException.Forbidden())

