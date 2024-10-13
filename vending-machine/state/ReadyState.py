from state.State import State
from state.vending_machine_state import VendingMachineState
from entity.transaction_entity import Purchaser
from db.db import PURCHASER_TABLE
from state.ProductDisplayState import ProductDisplayState

class ReadyState(State):
    def __init__(self, vending_machine) -> None:
        self._vending_machine = vending_machine
    def init(self) -> int:
        purchaser = Purchaser("IN_PROGRESS")
        PURCHASER_TABLE[purchaser.id] = purchaser
        self._vending_machine.change_state(ProductDisplayState(self))
        return purchaser.id
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
        return VendingMachineState.READY
