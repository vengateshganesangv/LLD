from state.State import State
from state.vending_machine_state import VendingMachineState

class ProductDispencing(State):
    def __init__(self, vending_machine) -> None:
        self._vending_machine = vending_machine
    def init(self) -> int:
        pass
    def show_product_details(self) -> None:
        pass
    def read_product_details(self, product_id: int, qty: int) -> None:
        pass
    def read_amount(self, purchaser_id: int, amount: float) -> None:
        pass
    def cancel_transaction(self, purchaser_id: int) -> bool:
        pass
    def cash_dispensing(self) -> None:
        pass
    def product_dispensing(self) -> None:
        pass
    def get_state_name(self) -> str:
        return VendingMachineState.PRODUCT_DISPENCING
