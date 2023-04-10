from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import SessionLocal, get_db

from models.comment import *
from models.task import *
from models.user import *
from models.solved import *

endpoint = APIRouter()


@endpoint.get("/tasks/")
def get_tasks(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Return by default maximum 25 tasks"""
    return db.query(TaskSchema).offset(offset).limit(limit).all()

@endpoint.get("/task/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Return task by ID"""
    return db.query(TaskSchema).filter(TaskSchema.id == task_id).first()

@endpoint.post("/task")
def create_task(task: TaskModel, db: Session = Depends(get_db)):
    db_task = TaskSchema(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
