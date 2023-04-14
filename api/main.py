from fastapi import FastAPI
from database import Base, engine



from endpoints import tasks
from endpoints import comments
from endpoints import user
from endpoints import solved
from fastapi.middleware.cors import CORSMiddleware
from middlewares.checkErrors import checkErrors

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Dodaj middleware, aby dodać nagłówek "Access-Control-Allow-Origin" do odpowiedzi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # zezwól na pobieranie zasobów z dowolnej domeny
    allow_credentials=True,
    allow_methods=["*"],  # zezwól na wszystkie metody HTTP
    allow_headers=["*"],  # zezwól na wszystkie nagłówki
)

# Middlewares
app.middleware("http")(checkErrors)

# Router
app.include_router(tasks.endpoint)
app.include_router(comments.endpoint)
app.include_router(user.endpoint)
app.include_router(solved.endpoint)
# HomePage
@app.get('/')
async def root():
    return {"message":"Hello World"}


