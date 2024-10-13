from dao.order_dao import OrderDAO
from dao.cart_dao import CartDAO
from dto.payment_repsonse_dto import PaymentResponseDTO
from entity.order_line_entity import OrderLine
from entity.shop_order import ShopOrder
from manager.abstract_cart_manager import AbstractCartManager
from manager.abstract_order_manager import AbstractOrderManager

class InMemoryOrderManager(AbstractOrderManager):
    def __init__(self):
        self.order_dao = OrderDAO()
        self.cart_dao = CartDAO()

    def _transfer_cart_to_order_line(self, order_id: int, cart_info):
        for cart in cart_info.products:
            order_line = OrderLine(cart.product_id, order_id, cart.price, cart.qty)
            self.order_dao.create_order_line(order_line)
        self.cart_dao = CartDAO()  # Clear the cart

    def place_order(self, cart_manager: AbstractCartManager, payment_response: PaymentResponseDTO, transaction_id: int) -> ShopOrder:
        cart_info = cart_manager.get_cart_info()
        new_order = ShopOrder(transaction_id, cart_info.total_amount, payment_response.amount_paid, payment_response.amount_to_refund)
        self.order_dao.create(new_order)
        self._transfer_cart_to_order_line(new_order.id, cart_info)
        return new_order

    def get_order_refund_value(self, order_id: int) -> int:
        order = self.order_dao.read(order_id)
        return order.amount_to_refund if order else 0

    def get_order_items(self, order_id: int) -> list[OrderLine]:
        return self.order_dao.get_order_lines(order_id)

