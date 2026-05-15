from app.domain.entities.order import Order


class CreateOrder:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, product, quantity):
        order = Order(product=product, quantity=quantity)

        self.repository.save(order)

        return order
