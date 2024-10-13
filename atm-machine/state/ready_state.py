from exception import IllegalStateError
from state.state import State
from state.atm_state import ATMState
from db.db_accessor import DBAccessor

class ReadyState(State):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        trans_id = DBAccessor.create_new_transaction(self.atm.get_machine_id())
        if trans_id == 0:
            raise RuntimeError("Unable to start transaction")
        self.atm.change_state(ATMState.CARD_READING)
        return trans_id

    def read_card(self, card_details):
        raise IllegalStateError("Currently in ready state, can't read card")

    def cancel_transaction(self, trans_id):
        raise IllegalStateError("No Transaction in progress")

    def read_withdrawal_details(self, card_details, trans_id, amount):
        raise IllegalStateError("Currently in ready state, can't read WithdrawalDetails")

    def dispense_cash(self, trans_id):
        raise IllegalStateError("Currently in ready state, can't dispense Cash")

    def eject_card(self):
        raise IllegalStateError("Currently in ready state, can't eject Card")

    def get_state_name(self):
        return ATMState.READY