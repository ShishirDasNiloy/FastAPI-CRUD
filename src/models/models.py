from sqlalchemy import Column, String
from models.base import BaseModel


class User(BaseModel):
    __tablename__='users'
    username=Column(String(20),nullable=False)
    email=Column(String(50),nullable=False, unique=True)
    phone = Column(String(20), nullable=True, unique=True)
    password = Column(String(20), nullable=True, unique=True)
    sex = Column(String(10), nullable=False)
    