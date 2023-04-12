from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends , HTTPException
from database import SessionLocal, get_db
from fastapi.responses import JSONResponse
from models.user import *

endpoint = APIRouter()


@endpoint.get("/user/{user_id}")
async def get_comments(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist.")
    return user
    


