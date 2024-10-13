from custom_enum.transaction_status_enum import TransactionStatusEnum
from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from entity.transaction_entity import Transaction
from state.abstract_vending_machine_action import State
from db.db import TRANSACTION_TABLE
from state.product_display_state import ProductDisplayState

class ReadyState(State):
    def __init__(self, vending_machine) -> None:
        self._vending_machine = vending_machine
    def init(self) -> int:
        transaction = Transaction(TransactionStatusEnum.PROCESSING)
        TRANSACTION_TABLE[transaction.id] = transaction
        self._vending_machine.change_state(ProductDisplayState(self._vending_machine))
        return transaction.id
    def show_product_details(self):
        pass
    def read_product_details(self, transaction_id, productDetails):
        pass
    def show_cart(self):
        pass
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