from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date

class Solved(Base):
    __tablename__ = "solved"
    id = Column(Integer,primary_key=True ,autoincrement=True)
    task_id = Column(Integer)
    solved_id = Column(Integer)
    date = Column(Date)


    