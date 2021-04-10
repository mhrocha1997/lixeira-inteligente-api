from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Text
from sqlalchemy.orm import relationship

from database import Base

from .Discard import discard_table
class Product(Base):
    __tablename__= "products"

    id = Column(Integer, primary_key=True, index=True)
    bar_code = Column(Integer) 
    name = Column(String, index=True)
    material = Column(String)
    weight = Column(DECIMAL(4,4), nullable=False)
    img_base64 = Column(Text(), nullable=True)
    points = Column(Integer, nullable=True)

    owners = relationship("User",secondary=discard_table, back_populates="products")