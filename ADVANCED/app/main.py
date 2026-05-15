from fastapi import FastAPI

from app.application.use_cases.create_order import CreateOrder
from app.infrastructure.repositories.sql_repository import SQLOrderRepository

app = FastAPI()


@app.post("/orders")
async def create_order():
    repo = SQLOrderRepository()

    use_case = CreateOrder(repo)

    return use_case.execute("Laptop", 2)
