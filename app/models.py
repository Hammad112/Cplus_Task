from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "Cplus"  # Table name updated

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
