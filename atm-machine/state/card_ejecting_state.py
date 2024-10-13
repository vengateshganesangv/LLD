from exception import IllegalStateError
from state.state import State
from state.atm_state import ATMState
from state.ready_state import ReadyState

class CardEjectingState(State):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateError()

    def read_card(self, card_details):
        raise IllegalStateError()

    def cancel_transaction(self, trans_id):
        raise IllegalStateError()

    def read_withdrawal_details(self, card_details, trans_id, amount):
        raise IllegalStateError()

    def dispense_cash(self, trans_id):
        raise IllegalStateError()

    def eject_card(self):
        self.atm.change_state(ATMState.READY)

    def get_state_name(self):
        return ATMState.CARD_EJECTING