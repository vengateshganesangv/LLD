from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from apis.get_product_list_API import GetProductListAPI
from state.products_details_reading import ProductsDetailsReading
from state.abstract_vending_machine_action import State

class ProductDisplayState(State):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine
    def init(self):
        pass
    def show_product_details(self):
        products = GetProductListAPI().get_product_list()
        self._vending_machine.change_state(ProductsDetailsReading(self._vending_machine))
        return products
    def read_product_details(self, transaction_id, productDetails):
        pass
    def show_cart(self):
        pass
    def place_order(self, payment_info, payment_mode):
        pass
    def cancel_transaction(self, transaction_id: int) -> bool:
        pass
    def cash_dispensing(self):
        pass
    def product_dispensing(self):
        pass
    def get_state(self):
        return VendingMachineStateEnum.PRODUCT_DISPLAY
