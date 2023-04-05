from sqlalchemy import Column, Integer, String, Date
from database import Base

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title =Column(String(255))
    author = Column(String(150))
    description = Column(String(255))
    lvl = Column(Integer)
    status = Column(String(255))
    count_Up = Column(Integer)
    count_Down = Column(Integer)
    data = Column(Date)
