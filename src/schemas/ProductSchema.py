from pydantic import BaseModel

class ProductSchema(BaseModel):
    email: str
    password: str
    name: str