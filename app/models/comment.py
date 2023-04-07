from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Boolean 

class Comment(Base):
    __tablename__ = "comment"
    id  = Column(Integer,primary_key=True ,autoincrement=True)
    taskid = Column(Integer)
    author = Column(String(200))
    date = Column(Date)
    comment = Column(String(250))
    rating = Column(Integer)
    isProtected = Column(Boolean)


class ModelComment(BaseModel):
    author: str = Field(min_length=1)
    comment: str = Field(min_length=1)
    rating: int = Field(gt = -1)
    isProtected: bool