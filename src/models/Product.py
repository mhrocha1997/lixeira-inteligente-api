from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Text
from sqlalchemy.orm import relationship

from database import Base

class Product(Base):
    __tablename__= "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    material = Column(String)
    weight = Column(DECIMAL(4,4), nullable=False)
    img_base64 = Column(Text(), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")