from dataclasses import dataclass


@dataclass
class Order:
    product: str
    quantity: int
