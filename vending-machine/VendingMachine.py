from dto.product_info_query_dto import ProductInfoQueryDTO
from factory.StateFactory import StateFactory
from db.db import MACHINE_TABLE
from state.abstract_vending_machine_action import State

class VendingMachine():
    def __init__(self, machine_id: int):
        self.machine_id = machine_id
        self.state : State = StateFactory.get_state(MACHINE_TABLE[self.machine_id].state, self)

    def init(self):
        return self.state.init()

    def cancel_transaction(self, transaction_id):
        return self.state.cancel_transaction(transaction_id)

    def show_product_details(self):
        return self.state.show_product_details()

    def read_product_details(self, transaction_id, product_list: ProductInfoQueryDTO):
        return self.state.read_product_details(transaction_id, product_list)
    
    def show_cart(self):
        return self.state.show_cart()

    def place_order(self, payment_info, payment_mode, transaction_id):
        return self.state.place_order( payment_info, payment_mode, transaction_id)

    def cash_dispensing(self):
        return self.state.cash_dispensing()

    def product_dispensing(self):
        return self.state.product_dispensing()

    def get_state(self):
        return self.state

    def get_machine_id(self):
        return self.machine_id

    def change_state(self, new_state):
        self.state = new_state
        MACHINE_TABLE[self.machine_id].state = new_state.get_state()