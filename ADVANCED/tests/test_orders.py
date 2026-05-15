from app.application.use_cases.create_order import CreateOrder


class FakeRepository:
    def save(self, order):
        self.order = order


def test_create_order():
    repo = FakeRepository()

    use_case = CreateOrder(repo)

    order = use_case.execute("Mouse", 1)

    assert order.product == "Mouse"
