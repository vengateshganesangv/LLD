from state.state import State
from state.atm_state import ATMState
from state.withdrawal_details_reading_state import WithdrawalDetailsReadingState
from state.ready_state import ReadyState
from card.card_manager_factory import CardManagerFactory
from db.db_accessor import DBAccessor
from exception import IllegalStateError

class CardReadingState(State):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateError()

    def read_card(self, card_details):
        result = CardManagerFactory.get_card_manager(card_details.get_card_type()).validate_card(card_details)
        DBAccessor.persist_card_details(card_details, self.atm.get_machine_id())
        if result:
            self.atm.change_state(ATMState.WITHDRAWAL_DETAILS_READING)
        else:
            DBAccessor.disapprove_transaction(self.atm.get_machine_id())
            self.atm.change_state(ATMState.READY)
        return True

    def cancel_transaction(self, trans_id):
        DBAccessor.cancel_transaction(trans_id)
        self.atm.change_state(ATMState.READY)
        return True

    def read_withdrawal_details(self, card_details, trans_id, amount):
        raise IllegalStateError()

    def dispense_cash(self, trans_id):
        raise IllegalStateError()

    def eject_card(self):
        raise IllegalStateError()

    def get_state_name(self):
        return ATMState.CARD_READING