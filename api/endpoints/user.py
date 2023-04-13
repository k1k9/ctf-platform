from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends , HTTPException
from database import SessionLocal, get_db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.user import *

endpoint = APIRouter()


@endpoint.get("/user/{user_id}")
async def get_comments(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist.")
    return jsonable_encoder(user)

@endpoint.get('/users/')
async def get_users(offset: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    """Return by default maximum 25 users"""
    users= db.query(UserSchema).offset(offset).limit(limit).all()
    response = {}
    for index,user in enumerate(users):
        response[index] = jsonable_encoder(user)
    return JSONResponse(response)


@endpoint.post("/user")
async def create_user(user: ModelUser, db: Session = Depends(get_db)):
    db_user = UserSchema(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    