import models
from datetime import datetime
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import engine, Sessionlocal
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()
    
class Task(BaseModel):
    title: str = Field(min_lenght =1)
    author: str = Field(min_lenght =1, max_lenght=255)
    description: str = Field(min_lenght =1, max_lenght=255)
    lvl:int = Field(gt =-1, lt=100)
    status:str = Field(min_lenght =1, max_lenght=255)
    count_Up:int = Field(gt =-1, lt=100)
    count_Down:int = Field(gt =-1, lt=100)
    
    

TASKS = []

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()

@app.post("/")
def create_task(task: Task, db: Session = Depends(get_db)):

    task_model = models.Tasks()
    task_model.title = task.title
    task_model.author = task.author
    task_model.description = task.description
    task_model.lvl = task.lvl
    task_model.status = task.status
    task_model.count_Up = task.count_Up
    task_model.count_Down = task.count_Down
    task_model.date = datetime.now()

    db.add(task_model)
    db.commit()

    return task

@app.put("/")
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):

    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()

    if task_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"id {task_id}: not exist"
        )
    task_model.title = task.title
    task_model.author = task.author
    task_model.description = task.description
    task_model.lvl = task.lvl
    task_model.status = task.status
    task_model.count_Up = task.count_Up
    task_model.count_Down = task.count_Down

    db.add(task_model)
    db.commit()

@app.delete("/")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()

    if task_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"id {task_id}: not exist"
        )
    
    db.query(models.Tasks).filter(models.Tasks.id == task_id).delete()
    db.commit()