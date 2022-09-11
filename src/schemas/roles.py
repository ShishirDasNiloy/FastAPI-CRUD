from pydantic import BaseModel
from typing import Optional


class UserIn(BaseModel):
    username: str
    email: str
    phone: str
    password: str
    sex: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    sex: Optional[str] = None



class UserOut(BaseModel):
    username: str
    email: str
    phone: str
    sex: str

    class Config:
        orm_mode = True



    


