from typing import List

from dao.in_memory_database_dao import InMemoryDatabase
from data.base_pizza import BasePizza
from data.pizza import Pizza
from data.topping_decorator import ToppingDecorator
from entity.order_item_entity import OrderItemEntity
from entity.pizza_entity import PizzaEntity
from entity.topping_entity import ToppingEntity

class PizzaService:
    def __init__(self, db: InMemoryDatabase):
        self.db = db

    def create_pizza(self, name: str, base_cost: float) -> PizzaEntity:
        return self.db.add_pizza(name, base_cost)

    def create_topping(self, name: str, cost: float) -> ToppingEntity:
        return self.db.add_topping(name, cost)

    def add_to_order(self, pizza_id: int, topping_ids: List[int]) -> OrderItemEntity:
        return self.db.add_order_item(pizza_id, topping_ids)

    def get_order_item(self, order_item_id: int) -> Pizza:
        order_item = self.db.get_order_item(order_item_id)
        if not order_item:
            return None
        
        pizza_entity = self.db.get_pizza(order_item.pizza_id)
        pizza = BasePizza(pizza_entity.name, pizza_entity.base_cost)
        
        for topping_id in order_item.topping_ids:
            topping_entity = self.db.get_topping(topping_id)
            pizza = ToppingDecorator(pizza, topping_entity.name, topping_entity.cost)
        
        return pizza