from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Text
from sqlalchemy.orm import relationship

from database import Base

class Bin(Base):

    id_bin = Column(INTEGER(unsigned=True), primary_key=True)
    address = Column(String(70), nullable=False)
    capacity = Column(INTEGER(unsigned=True), nullable=False)
    status = Column(INTEGER(unsigned=True), nullable=False)
    last_updated = Column(DateTime, nullable=False)