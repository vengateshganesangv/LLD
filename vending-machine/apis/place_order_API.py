# api/place_order_api.py
from custom_enum.database_name_enum import DatabaseNameEnum
from custom_enum.payment_mode_enum import PaymentModeEnum
from custom_enum.payment_status_enum import PaymentStatusEnum
from entity.shop_order import ShopOrder
from factory.cart_manager_factory import CartManagerFactory
from factory.order_manager_factory import OrderManagerFactory
from factory.payment_manager_factory import PaymentManagerFactory

class PlaceOrderAPI:
    def place_order(self, payment_info: dict[str, str], payment_mode: PaymentModeEnum, transaction_id: int) -> ShopOrder:
        order_manager = OrderManagerFactory.get_order_manager(DatabaseNameEnum.INMEMORY)
        cart_manager = CartManagerFactory.get_cart_manager(DatabaseNameEnum.INMEMORY)
        payment_manager = PaymentManagerFactory.get_payment_manager(payment_mode, payment_info)
        
        payment_response = payment_manager.process_payment(cart_manager)
        if payment_response.payment_status in [PaymentStatusEnum.EQUAL, PaymentStatusEnum.OVER_PAID]:
            payment_manager.execute_payment(payment_response)
        else:
            raise ValueError("Qualified Amount Not added")
        
        return order_manager.place_order(cart_manager, payment_response, transaction_id)