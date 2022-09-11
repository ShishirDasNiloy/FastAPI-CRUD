from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from sqlalchemy.sql import func
from database import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer(), primary_key = True, autoincrement = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())