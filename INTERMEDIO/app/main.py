from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.session import engine
from app.routers.auth import router as auth_router
from app.routers.orders import router as orders_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(auth_router)

app.include_router(orders_router)


@app.get("/")
async def root():
    return {"message": "FastAPI Orders API"}
