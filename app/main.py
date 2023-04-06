from fastapi import FastAPI
from database import Base, engine

from routers import tasks as TaskRouter
from middlewares.checkErrors import checkErrors

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Middlewares
app.middleware("http")(checkErrors)

# Router
app.include_router(TaskRouter.router)

# HomePage
@app.get('/')
async def root():
    return {"message":"Hello World"}