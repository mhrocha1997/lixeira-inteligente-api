from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from database import Base

discard_table = Table('discards', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('quantity', Integer,nullable=True)
)