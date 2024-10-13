from exception import IllegalStateError
from state.state import State
from state.atm_state import ATMState
from state.cash_dispensing_state import CashDispensingState
from state.card_ejecting_state import CardEjectingState
from card.card_manager_factory import CardManagerFactory
from card.transaction_status import TransactionStatus
from db.db_accessor import DBAccessor

class WithdrawalDetailsReadingState(State):
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
        res = CardManagerFactory.get_card_manager(card_details.get_card_type()).validate_withdrawal(amount, trans_id)
        if res:
            self.atm.change_state(ATMState.CASH_DISPENSING)
            DBAccessor.persist_with_details(trans_id, amount, TransactionStatus.APPROVED)
        else:
            self.atm.change_state(ATMState.CARD_EJECTING)
            DBAccessor.persist_with_details(trans_id, amount, TransactionStatus.NOT_APPROVED)
        return res

    def dispense_cash(self, trans_id):
        raise IllegalStateError()

    def eject_card(self):
        raise IllegalStateError()

    def get_state_name(self):
        return ATMState.WITHDRAWAL_DETAILS_READING