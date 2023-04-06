from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Boolean 

class Comment(Base):
    id  = Column(Integer, autoincrement=True)
    taskid = Column(Integer)
    author = Column(String(200))
    date = Column(Date)
    comment = Column(String(250))
    rating = Column(Integer)
    isProtected = Column(Boolean)