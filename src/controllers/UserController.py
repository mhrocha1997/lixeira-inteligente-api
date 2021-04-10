from sqlalchemy.orm import Session

from models import User
from schemas import UserSchema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db:Session, user: UserSchema):
