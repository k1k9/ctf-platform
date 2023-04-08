from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey 
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comment"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    task = relationship("Task", back_populates="comments")
    task_id = Column(Integer, ForeignKey("task.id"))
    
    user = relationship("User", back_populates="comments")
    user_id = Column(Integer, ForeignKey("user.id"))
    
    author = Column(String(200))
    date = Column(Date)
    comment = Column(String(250))
    rating = Column(Integer)
    is_protected = Column(Boolean)

class ModelComment(BaseModel):
    author: str = Field(min_length=1)
    comment: str = Field(min_length=1)
    rating: int = Field(gt=-1)
    is_protected: bool
    task_id: int = Field(gt=-1)
    user_id: int = Field(gt=-1)