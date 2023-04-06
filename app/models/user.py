from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Boolean

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True ,nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    salt = Column(String(20), nullable=False)
    email = Column(String(30))
    image = Column(String(200))
    description = Column(String(200))
    points = Column(Integer)
    ranking = Column(Integer(200))
    newsletter = Column(String(200))
    rank = Column(String(100))
    premium = Column(Boolean)