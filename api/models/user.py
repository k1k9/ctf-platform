from database import Base
from pydantic import BaseModel, Field , EmailStr, validator
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class UserSchema(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    solved = relationship("SolvedSchema", back_populates="user")
    comments = relationship("CommentSchema", back_populates="user")
    task = relationship("TaskSchema", back_populates="user")
    username = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    #salt = Column(String(20))
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
    email: EmailStr
    image: str = Field(min_length=1)
    description: str = Field(min_length=1)
    points: int = Field(gt=-1)
    user_rank: str = Field(min_length=1)
    newsletter: str = Field(min_length=1)
    premium: bool
    
    @validator('username')
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError('only alphanumeric characters')
        return v

    @validator('nickname')
    def validate_nickname(cls, v):
        if not v.isalnum():
            raise ValueError('only alphanumeric characters')
        return v