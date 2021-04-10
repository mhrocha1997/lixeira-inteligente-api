from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Text, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Bin(Base):
    __tablename__ = "bins"

    id_bin = Column(Integer, primary_key=True)
    address = Column(String(70), nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False)
    hub_id = Column(Integer, ForeignKey("hubs.id"))

    hub = relationship("Hub", back_populates="bins")