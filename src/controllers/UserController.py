from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from models import User
from schemas import UserSchema as sch

from database import Base, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@router.post("/create/")
def create_user(request: sch.UserCreate, db: Session = Depends(get_db)):
    """
        Cadastro do usuário
    """
    try:
        new_user = User(
            name=request.name,
            email=request.email,
            password=request.password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user.id
    except Exception as e:
        print(e)

# @router.post("/login")
# def login():
#     """
#         Login do usuário. Entra com e-mail e senha e recebe um token de autenticação
#     """
#     try:

#     except Exception as e:
#         print(e)

