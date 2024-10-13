from data.pizza import Pizza

class BasePizza(Pizza):
    def __init__(self, name: str, cost: float):
        self._name = name
        self._cost = cost

    def get_description(self) -> str:
        return self._name

    def get_cost(self) -> float:
        return self._cost