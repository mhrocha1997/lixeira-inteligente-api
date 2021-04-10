from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from database import Base

class Hub(Base):
    __tablename__= "hubs"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ip = Column(String(15), nullable=False)
    address = Column(String(70), nullable=False)

    bins = relationship("Bin", back_populates="hub")

