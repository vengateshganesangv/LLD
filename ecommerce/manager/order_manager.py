from data.order import Order
from data.order_status import OrderStatus
from data.user import User
from db.db_accessor import DBAccessor
from manager.cart_manager import CartManager


class OrderManager:
    def place_order(self, user: User) -> Order:
        cart_manager = CartManager()
        cart_items = cart_manager.get_cart(user)
        order_id = DBAccessor.create_order(user, cart_items)
        cart_manager.checkout_cart(user)

        return Order(cart_items, order_id, user.get_id(), OrderStatus.ORDER_PLACED)

    def get_orders(self, user: User):
        return None

    def get_order(self, order_id: int):
        return None
