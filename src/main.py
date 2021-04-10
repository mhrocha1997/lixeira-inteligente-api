from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models import User
from schemas import UserSchema

from database import engine, Base, SessionLocal

Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@app.get("/")
def test():
    return {"message": "OK"}


@app.post("/create/user")
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    """
        Cadastro do usuário
    """
    try:
        new_user = User(name=request.name,email=request.email,password=request.password,)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user.id
    except Exception as e:
        print(e)

