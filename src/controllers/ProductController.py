from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from models import Product
from schemas import ProductSchema

from database import engine, Base, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@router.post("/create/")
def create_product(request: ProductSchema, db: Session = Depends(get_db)):
    """
        Cadastro do usuário
    """
    try:
        new_product = Product(name=request.name,email=request.email,password=request.password,)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product.id
    except Exception as e:
        print(e)