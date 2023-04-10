from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime, func , Boolean, ForeignKey 
from sqlalchemy.orm import relationship

class CommentSchema(Base):
    __tablename__ = "comment"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    task_id = Column(Integer, ForeignKey("task.id"))
    task = relationship("TaskSchema", back_populates="comments")
    
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserSchema", back_populates="comments")
    
    author = Column(String(200))
    date = Column(DateTime, default=func.now())
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