from fastapi import FastAPI
from database import Base, engine
from routers import tasks as TaskRouter

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Router
app.include_router(TaskRouter.router)

# HomePage
@app.get('/')
async def root():
    return {"message":"Hello World"}