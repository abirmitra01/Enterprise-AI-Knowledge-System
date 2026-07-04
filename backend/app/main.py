from fastapi import FastAPI
from app.api.routes import router
from app.core.config import PROJECT_NAME, VERSION
from app.databases.postgres import engine, Base
from app.models.user import User
from app.api.auth import router as auth_router
from app.models import user
from app.models import document
from app.api.upload import router as upload_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(search_router)
app.include_router(chat_router)
