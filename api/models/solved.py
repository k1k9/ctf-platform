from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, DateTime, func , ForeignKey
from sqlalchemy.orm import relationship


class SolvedSchema(Base):

    __tablename__ = "solved"

    id = Column(Integer,primary_key=True ,autoincrement=True)
    task = relationship("TaskSchema", back_populates="solved")
    task_id = Column(Integer, ForeignKey("task.id"))
    date = Column(DateTime, default=func.now())
    user = relationship("UserSchema", back_populates="solved")
    user_id = Column(Integer, ForeignKey("user.id"))
    

class ModelSolved(BaseModel):
    task_id: int = Field(gt=-1)
    solved_id: int
     