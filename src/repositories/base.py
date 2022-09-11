from typing import Any, Generic, Optional, Type, TypeVar, List, Union
from unittest import result
from sqlalchemy.orm import Session
from database import Base
import database
from models import BaseModel

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)

class BaseRepo(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, database: Session, data_in: CreateSchemaType) -> ModelType:
        data = self.model(**data_in.dict())
        database.add(data)
        database.commit()
        database.refresh(data)
        return data

    def get(self, database:Session) ->List[ModelType]:
        query = database.query(self.model).all()
        return query


    def get_one(self, database: Session, id: int) -> ModelType:
        return database.query(self.model).filter(self.model.id == id).first()

    def update(self, database: Session, id:int, data_update: UpdateSchemaType) -> ModelType:
        database.query(self.model).filter(self.model.id == id).update(data_update.dict(exclude_unset=True), synchronize_session=False)
        database.commit()
        return self.get_one(database,id)

    def delete(self, database:Session, id:int) -> Optional[Union[ModelType, Any]]:
        result = database.query(self.model). filter(self.model.id == id).delete(synchronize_session=False)
        database.commit()
        return result

