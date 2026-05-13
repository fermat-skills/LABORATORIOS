from fastapi import APIRouter

from app.core.security import create_access_token
from app.schemas.auth import LoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(data: LoginRequest):
    token = create_access_token({"sub": data.username})

    return {"access_token": token}
