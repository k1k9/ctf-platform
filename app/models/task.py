from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date  
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    solved_t = relationship('Solved', back_populates="task")
    comment_id = relationship('Comment',back_populates='task')
    title =Column(String(255),unique=True)
    reward = Column(String(150))
    lvl = Column(Integer)
    content = Column(String(255))
    solution = Column(String(250))
    solvers = Column(String(250))
    rating = Column(String(250))
    category = Column(String(250))
    status = Column(String(255))
    author = Column(String(200))
    date = Column(Date)

class Model(BaseModel):
    title: str = Field(min_lenght =1)
    reward: str = Field(min_lenght =1, max_lenght=150)
    lvl:int = Field(qt = -1, lt =5)
    author: str = Field(min_lenght =1, max_lenght=255)
    content: str = Field(min_lenght =1, max_lenght=255)
    solution: str = Field(min_lenght =1, max_lenght=255)
    solvers: str = Field(min_lenght =1, max_lenght=255)
    rating:int = Field(qt =-1, lt =5)
    category: str = Field(min_lenght =1, max_lenght=255)
    status:str = Field(min_lenght =1, max_lenght=255)
    author: str = Field(min_lenght =1, max_lenght=255)
    