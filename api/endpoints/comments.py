from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends , HTTPException
from database import SessionLocal, get_db
from fastapi.responses import JSONResponse
from models.comment import *

endpoint = APIRouter()

# TODO zabezpieczyc tokenem przed smiertelnikiem
@endpoint.get("/commnets/{task_id}")
async def get_commnets(task_id:int, db: Session = Depends(get_db)):
    comment = db.query(CommentSchema).filter(CommentSchema.task_id == task_id).first()
    if not comment:
       raise HTTPException(status_code=404, detail="Comment doesnt't exist")
    return comment


@endpoint.post("/comments")
async def create_comment(comment: CommentModel, db: Session = Depends(get_db)):
    db_comment = CommentSchema(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@endpoint.delete("/comment/{comment_id}/delete")
async def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(CommentSchema).filter(CommentSchema.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)
    db.commit()
    return {"message": "Comment deleted successfully"}

