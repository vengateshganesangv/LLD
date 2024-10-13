from apis.get_cart_info_API import GetCartInfoAPI
from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from state.abstract_vending_machine_action import State
from state.place_order_state import PlaceOrderState

class ShowCartState(State):
    def __init__(self, vending_machine) -> None:
        self._vending_machine = vending_machine
    def init(self) -> int:
        pass
    def show_product_details(self):
        pass
    def read_product_details(self):
        pass
    def show_cart(self):
        cart_info = GetCartInfoAPI().get_cart_product_info()
        self._vending_machine.change_state(PlaceOrderState(self._vending_machine))
        return cart_info
    def place_order(self, payment_info, payment_mode):
        pass
    def cancel_transaction(self, transaction_id):
        pass
    def cash_dispensing(self):
        pass
    def product_dispensing(self):
        pass
    def get_state(self):
        return VendingMachineStateEnum.READY
