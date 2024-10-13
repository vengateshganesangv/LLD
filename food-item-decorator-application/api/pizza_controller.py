from service.pizza_service import PizzaService


class PizzaController:
    def __init__(self, pizza_service: PizzaService):
        self.pizza_service = pizza_service

    def create_pizza(self, name: str, base_cost: float) -> dict:
        pizza = self.pizza_service.create_pizza(name, base_cost)
        return {'id': pizza.id, 'name': pizza.name, 'base_cost': pizza.base_cost}

    def create_topping(self, name: str, cost: float) -> dict:
        topping = self.pizza_service.create_topping(name, cost)
        return {'id': topping.id, 'name': topping.name, 'cost': topping.cost}

    def add_to_order(self, pizza_id: int, topping_ids: list[int]) -> dict:
        order_item = self.pizza_service.add_to_order(pizza_id, topping_ids)
        return {'order_item_id': order_item.id}

    def get_order_item(self, order_item_id: int) -> dict:
        pizza = self.pizza_service.get_order_item(order_item_id)
        if not pizza:
            return {'error': 'Order item not found'}
        return {
            'description': pizza.get_description(),
            'total_cost': pizza.get_cost()
        }