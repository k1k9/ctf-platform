from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date

class Solved(Base):
    id = Column(Integer, autoincrement=True)
    task_id = Column(Integer)
    solved_id = Column(Integer)
    date = Column(Date)
