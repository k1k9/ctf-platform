from database import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException
from models.solved import *



endpoint = APIRouter()



@endpoint.get('/solved/{solved_id}')
async def get_solved(solved_id: int, db:Session = Depends(get_db)):
    solved = db.query(SolvedSchema).filter(SolvedSchema.id == solved_id).first()
    if not solved:
        raise HTTPException(status_code=404, detail="Nobody solved it")
    return jsonable_encoder(solved)