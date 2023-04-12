from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import SessionLocal, get_db
from fastapi.responses import JSONResponse
from models.comment import *

endpoint = APIRouter()

# TODO zabezpieczyc tokenem przed smiertelnikiem
@endpoint.get("/commnets/{task_id}")
def get_commnets(task_id:int, db: Session = Depends(get_db)):
    return db.query(CommentSchema).filter(CommentSchema.task_id == task_id).first()

