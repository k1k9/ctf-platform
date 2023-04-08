from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Solved(Base):

    __tablename__ = "solved"

    id = Column(Integer,primary_key=True ,autoincrement=True)

    task1 = relationship("Task", back_populates="solved_t")
    task_id = Column(Integer, ForeignKey("task.id"))

    date = Column(Date)

    solved_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="solved")
    

class ModelSolved(BaseModel):
    task_id: int = Field(gt=-1)
    solved_id: int
     