from fastapi import FastAPI
from database import Base, engine

from endpoints import tasks
from endpoints import comments
from endpoints import user

from middlewares.checkErrors import checkErrors

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Middlewares
app.middleware("http")(checkErrors)

# Router
app.include_router(tasks.endpoint)
app.include_router(comments.endpoint)
app.include_router(user.endpoint)
# HomePage
@app.get('/')
async def root():
    return {"message":"Hello World"}