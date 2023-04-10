from fastapi import FastAPI
from database import Base, engine

from endpoints.tasks import *
from middlewares.checkErrors import checkErrors

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Middlewares
app.middleware("http")(checkErrors)

# Router
app.include_router(endpoint)

# HomePage
@app.get('/')
async def root():
    return {"message":"Hello World"}