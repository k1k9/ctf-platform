from database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date

class Schema(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title =Column(String(255),unique=True)
    reward = Column(String(150))
    description = Column(String(255))
    lvl = Column(Integer)
    status = Column(String(255))
    count_Up = Column(Integer)
    count_Down = Column(Integer)
    date = Column(Date)

class Model(BaseModel):
    title: str = Field(min_lenght =1)
    author: str = Field(min_lenght =1, max_lenght=255)
    description: str = Field(min_lenght =1, max_lenght=255)
    lvl:int = Field(gt =-1, lt=100)
    status:str = Field(min_lenght =1, max_lenght=255)
    count_Up:int = Field(gt =-1, lt=100)
    count_Down:int = Field(gt =-1, lt=100)