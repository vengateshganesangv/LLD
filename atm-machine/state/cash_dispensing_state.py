from card.card_type import CardType
from exception import IllegalStateError
from state.state import State
from state.atm_state import ATMState
from state.card_ejecting_state import CardEjectingState
from card.card_manager_factory import CardManagerFactory
from db.db_accessor import DBAccessor

class CashDispensingState(State):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateError()

    def read_card(self, card_details):
        raise IllegalStateError()

    def cancel_transaction(self, trans_id):
        DBAccessor.cancel_transaction(trans_id)
        self.atm.change_state(ATMState.CARD_EJECTING)
        return True

    def read_withdrawal_details(self, card_details, trans_id, amount):
        raise IllegalStateError()

    def dispense_cash(self, trans_id):
        # Note: card_type should be retrieved from the transaction details
        card_type = CardType.DEBIT  # This should be implemented
        CardManagerFactory.get_card_manager(card_type).execute_withdrawal(trans_id)
        self.atm.change_state(ATMState.CARD_EJECTING)
        return DBAccessor.mark_as_exec(trans_id)

    def eject_card(self):
        raise IllegalStateError()

    def get_state_name(self):
        return ATMState.CASH_DISPENSING