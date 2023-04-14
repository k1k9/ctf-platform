from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends , HTTPException
from database import SessionLocal, get_db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
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




"""All Hash for pwd and salt"""
hash_passw = CryptContext(schemes=["bcrypt"], deprecated="auto")

@endpoint.post("/user")
async def create_user(user: ModelUser, db: Session = Depends(get_db)):
    hashed_password = hash_passw.hash(user.password)
    db_user = UserSchema(username=user.username, nickname=user.nickname, password=hashed_password, email=user.email, image=user.image, description=user.description, points=user.points, user_rank=user.user_rank, newsletter=user.newsletter, premium=user.premium)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@endpoint.delete("/user/{user_id}/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    db.delete(db_user)
    db.commit()
    return {"message": "Account deleted successfully"}