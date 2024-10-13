from apis.add_to_cart_API import AddToCartAPI
from apis.get_cart_info_API import GetCartInfoAPI
from dto.product_info_query_dto import ProductInfoQueryDTO
from state.abstract_vending_machine_action import State
from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from state.show_cart_state import ShowCartState

class ProductsDetailsReading(State):
    def __init__(self, vending_machine) -> None:
        self._vending_machine = vending_machine
    def init(self) -> int:
        pass
    def show_product_details(self) -> None:
        pass
    def read_product_details(self, transation_id, product_details: list[ProductInfoQueryDTO]):
        isSuccess = AddToCartAPI().add_to_cart(transation_id, product_details)
        self._vending_machine.change_state(ShowCartState(self._vending_machine))
        return isSuccess
    def show_cart(self):
        pass
    def place_order(self, payment_info, payment_mode):
        pass
    def cancel_transaction(self, transaction_id: int):
        pass
    def cash_dispensing(self):
        pass
    def product_dispensing(self):
        pass
    def get_state(self):
        return VendingMachineStateEnum.PRODUCT_DETAILS_READING
