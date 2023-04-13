from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float ,DateTime, func, Text, ForeignKey
from sqlalchemy.orm import relationship


class TaskSchema(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserSchema", back_populates="task")
    comments = relationship('CommentSchema', back_populates='task')
    solved = relationship('SolvedSchema', back_populates="task")
    title = Column(String(255),unique=False)
    reward = Column(Integer)
    lvl = Column(String(9))
    content = Column(Text)
    solution = Column(String(255))
    solvers = Column(Integer)
    rating = Column(Float)
    category = Column(String(30))
    status = Column(String(15))
    date = Column(DateTime, default=func.now())
    

class TaskModel(BaseModel):
    user_id: int = Field(gt=-1)
    title: str = Field(min_length=1)
    reward: int = Field(gt=-1, lt=80)
    lvl: str = Field(min_length=1, max_length=9)
    content: str = Field(min_length=10)
    solution: str = Field(min_length=1, max_length=255)
    solvers: int = Field(gt=-1)
    rating: float = Field(gt=-1, lt=5, round=2)
    category: str = Field(min_length=1, max_length=30)
    status: str = Field(min_length=1, max_length=15)