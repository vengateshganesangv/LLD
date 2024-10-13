from api.pizza_controller import PizzaController
from dao.in_memory_database_dao import InMemoryDatabase
from service.pizza_service import PizzaService


def main():
    db = InMemoryDatabase()
    pizza_service = PizzaService(db)
    pizza_controller = PizzaController(pizza_service)

    # Create pizzas and toppings
    margherita = pizza_controller.create_pizza("Margherita", 10)
    mushrooms = pizza_controller.create_topping("Mushrooms", 2)
    extra_cheese = pizza_controller.create_topping("Extra Cheese", 3)

    # Add to order
    order = pizza_controller.add_to_order(margherita['id'], [mushrooms['id'], extra_cheese['id']])

    # Get order details
    order_details = pizza_controller.get_order_item(order['order_item_id'])
    print(f"Order: {order_details['description']}")
    print(f"Total Cost: ${order_details['total_cost']}")

if __name__ == "__main__":
    main()