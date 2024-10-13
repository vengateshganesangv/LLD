from entity.order_item_entity import OrderItemEntity
from entity.pizza_entity import PizzaEntity
from entity.topping_entity import ToppingEntity


class InMemoryDatabase:
    def __init__(self):
        self.pizzas: dict[int, PizzaEntity] = {}
        self.toppings: dict[int, ToppingEntity] = {}
        self.order_items: dict[int, OrderItemEntity] = {}
        self.next_id = {'pizza': 1, 'topping': 1, 'order_item': 1}

    def add_pizza(self, name: str, base_cost: float) -> PizzaEntity:
        pizza = PizzaEntity(self.next_id['pizza'], name, base_cost)
        self.pizzas[pizza.id] = pizza
        self.next_id['pizza'] += 1
        return pizza

    def add_topping(self, name: str, cost: float) -> ToppingEntity:
        topping = ToppingEntity(self.next_id['topping'], name, cost)
        self.toppings[topping.id] = topping
        self.next_id['topping'] += 1
        return topping

    def add_order_item(self, pizza_id: int, topping_ids: list[int]) -> OrderItemEntity:
        order_item = OrderItemEntity(self.next_id['order_item'], pizza_id, topping_ids)
        self.order_items[order_item.id] = order_item
        self.next_id['order_item'] += 1
        return order_item

    def get_pizza(self, pizza_id: int) -> PizzaEntity:
        return self.pizzas.get(pizza_id)

    def get_topping(self, topping_id: int) -> ToppingEntity:
        return self.toppings.get(topping_id)

    def get_order_item(self, order_item_id: int) -> OrderItemEntity:
        return self.order_items.get(order_item_id)