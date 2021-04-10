from pydantic import BaseModel

class ProductSchema(BaseModel):
    bar_code: int
    name: str
    material: str
    weight: float
    points: int