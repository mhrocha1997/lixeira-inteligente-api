from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from models import User
from schemas import UserSchema
from controllers import UserRouter, ProductRouter

from database import engine, Base, SessionLocal

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=['Test Connection'])
def test():
    return {"message": "OK"}

app.include_router(
    UserRouter, 
    prefix="/user", 
    tags=['User']
)

app.include_router(
    ProductRouter, 
    prefix="/product", 
    tags=["Product"]
)