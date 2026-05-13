from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.schemas.orders import OrderCreate, OrderOut

router = APIRouter(prefix="/orders", tags=["orders"])

fake_db: list[dict[str, int | str]] = []


@router.post("/", response_model=OrderOut)
async def create_order(order: OrderCreate, user=Depends(get_current_user)):
    new_order: dict[str, int | str] = {
        "id": len(fake_db) + 1,
        "product": order.product,
        "quantity": order.quantity,
    }

    fake_db.append(new_order)

    return new_order


@router.get("/")
async def get_orders():
    return fake_db
