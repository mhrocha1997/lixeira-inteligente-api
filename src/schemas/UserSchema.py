from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str

class UserCreate(UserBase):
    name: str