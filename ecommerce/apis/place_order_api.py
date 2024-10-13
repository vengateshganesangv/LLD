from data.order import Order
from data.payment_response import PaymentResponse
from data.payment_status import PaymentStatus
from data.user import User
from factory.payment_manager_factory import PaymentManagerFactory
from manager.order_manager import OrderManager

class PlaceOrderAPI:
    def __init__(self, order_manager: OrderManager):
        self.order_manager = order_manager

    def place_order(self, user: User, payment_info: dict, payment_mode: str) -> Order:
        payment_manager = PaymentManagerFactory.get_payment_manager(payment_mode, payment_info)
        payment_response: PaymentResponse = payment_manager.execute_payment()

        if payment_response.status != PaymentStatus.SUCCESS:
            raise RuntimeError("Payment failed")

        return self.order_manager.place_order(user)