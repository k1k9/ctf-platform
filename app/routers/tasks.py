from models import task as Task, user as User, comment as Comment, solved as Solved
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import SessionLocal, get_db


router = APIRouter()


@router.get("/tasks/")
def get_tasks(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Return by default maximum 25 tasks"""
    return db.query(Task.Task).offset(offset).limit(limit).all()

@router.get("/task/{task_id}")
def get_tasks(task_id: int, db: Session = Depends(get_db)):
    """Return task by ID"""
    return db.query(Task.Model).filter(Task.Model.id == task_id).first()

@router.post("/task")
def create_task(task: Task.Model, db: Session = Depends(get_db)):
    db_task = Task.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
