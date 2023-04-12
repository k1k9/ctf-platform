from database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException

# Modules
from models.task import *
from models.user import *
from models.solved import *

endpoint = APIRouter()


@endpoint.get("/tasks/")
async def get_tasks(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    """Return by default maximum 25 tasks"""
    tasks = db.query(TaskSchema).offset(offset).limit(limit).all()
    response = {}
    for index,task in enumerate(tasks):
        response[index] = jsonable_encoder(task)
    return JSONResponse(response)



@endpoint.get("/task/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """Return task by ID"""
    task = db.query(TaskSchema).filter(TaskSchema.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task dosen't exist")
    return jsonable_encoder(task)

@endpoint.post("/task")
async def create_task(task: TaskModel, db: Session = Depends(get_db)):
    db_task = TaskSchema(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@endpoint.delete("/task/{task_id}/delete")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskSchema).filter(TaskSchema.id  == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}


@endpoint.put("/task/{task_id}/update")
def update_task(task_id: int, task: TaskModel, db: Session = Depends(get_db)):
    db_task = db.query(TaskSchema).filter(TaskSchema.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title
    db_task.reward = task.reward
    db_task.content = task.content
    db_task.category = task.category
    db.commit()
    db.refresh(db_task)
    return db_task




