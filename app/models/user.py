from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    solved = relationship("Solved", back_populates="user")
    username = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    salt = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    image = Column(String(200))
    description = Column(String(200))
    points = Column(Integer)
    newsletter = Column(String(200))
    user_rank = Column(String(100))
    premium = Column(Boolean)
    

class ModelUser(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    nickname: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8, max_length=20)
    email: str = Field(min_length=4, max_length=10)
    image: str = Field(min_length=1)
    description: str = Field(min_length=1)
    points: int = Field(gt=-1)
    user_rank: str = Field(min_length=1)
    newsletter: str = Field(min_length=1)
    premium: bool