from sqlalchemy import Boolean, Column, Integer, String
from .database import Base


class Product(Base):
    __productmaterial__ = "materials"

    id = Column(Integer, primary_key=True)
    material = Column(String, unique=True)
    size = Column(String)
