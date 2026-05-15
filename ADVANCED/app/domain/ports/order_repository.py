from typing import Protocol

from app.domain.entities.order import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        """
        Guarda una orden.
        """
        ...

    def get_all(self) -> list[Order]:
        """
        Obtiene todas las órdenes.
        """
        ...

    def get_by_id(self, order_id: int) -> Order | None:
        """
        Busca una orden por ID.
        """
        ...

    def delete(self, order_id: int) -> None:
        """
        Elimina una orden por ID.
        """
        ...

    def update(self, order: Order) -> None:
        """
        Actualiza una orden existente.
        """
        ...
