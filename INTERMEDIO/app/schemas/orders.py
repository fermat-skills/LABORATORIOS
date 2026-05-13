from pydantic import BaseModel


class OrderCreate(BaseModel):
    product: str

    quantity: int


class OrderOut(BaseModel):
    id: int

    product: str

    quantity: int

    class Config:
        from_attributes = True
