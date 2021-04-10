from fastapi import Depends, APIRouter, File, UploadFile
from sqlalchemy.orm import Session
import base64

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
def create_product(request: ProductSchema, db: Session = Depends(get_db), product_img: UploadFile = File(...)):
    """
        Cadastro de produto
    """
    try:
    
        img_base64 = base64.b64encode(product_img.file)

        new_product = Product(
            bar_code=request.bar_code,
            material=request.material,
            weight=request.weight,
            points=request.points,
            img_base64=img_base64
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product.id
    except Exception as e:
        print(e)

