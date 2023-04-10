from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime, func 
from sqlalchemy.orm import relationship




class TaskSchema(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    comments = relationship('CommentSchema', back_populates='task')
    solved = relationship('SolvedSchema', back_populates="task")
    title = Column(String(255),unique=True)
    reward = Column(String(150))
    lvl = Column(Integer)
    content = Column(String(255))
    solution = Column(String(250))
    solvers = Column(String(250))
    rating = Column(String(250))
    category = Column(String(250))
    status = Column(String(255))
    author = Column(String(200))
    date = Column(DateTime, default=func.now())
    
    


class TaskModel(BaseModel):
    title: str = Field(min_length=1)
    reward: str = Field(min_length=1, max_length=150)
    lvl: int = Field(gt=-1, lt=5)
    author: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1, max_length=255)
    solution: str = Field(min_length=1, max_length=255)
    solvers: str = Field(min_length=1, max_length=255)
    rating: int = Field(gt=-1, lt=5)
    category: str = Field(min_length=1, max_length=255)
    status: str = Field(min_length=1, max_length=255)
