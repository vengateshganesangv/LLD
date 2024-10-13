from data.pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza, name: str, cost: float):
        self._pizza = pizza
        self._name = name
        self._cost = cost

    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, {self._name}"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + self._cost