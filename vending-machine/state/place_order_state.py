from apis.place_order_API import PlaceOrderAPI
from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from state.abstract_vending_machine_action import State

class PlaceOrderState(State):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine
    def init(self):
        pass
    def show_product_details(self):
        pass
    def read_product_details(self, transaction_id, productDetails):
        pass
    def show_cart(self):
        pass
    def place_order(self, payment_info, payment_mode, transaction_id):
        shop_order = PlaceOrderAPI().place_order(payment_info, payment_mode, transaction_id)
        return shop_order
    def cancel_transaction(self, transaction_id: int) -> bool:
        pass
    def cash_dispensing(self):
        pass
    def product_dispensing(self):
        pass
    def get_state(self):
        return VendingMachineStateEnum.PLACE_ORDER
