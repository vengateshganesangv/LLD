from db.db_accessor import DBAccessor
from state.atm_state import ATMState
from state.card_ejecting_state import CardEjectingState
from state.card_reading_state import CardReadingState
from state.cash_dispensing_state import CashDispensingState
from state.ready_state import ReadyState
from state.withdrawal_details_reading_state import WithdrawalDetailsReadingState

class ATM:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.state = self.get_state(DBAccessor.get_atm_state(self.machine_id))

    def init(self):
        return self.state.init()

    def cancel(self, trans_id):
        return self.state.cancel_transaction(trans_id)

    def read_card(self, card_details):
        return self.state.read_card(card_details)

    def read_withdrawal_details(self, card_details, trans_id, amount):
        return self.state.read_withdrawal_details(card_details, trans_id, amount)

    def dispense_cash(self, trans_id):
        return self.state.dispense_cash(trans_id)

    def eject_card(self):
        self.state.eject_card()

    def get_state(self):
        return self.state

    def get_machine_id(self):
        return self.machine_id

    def get_state(self, atm_state):
        state_classes = {
            ATMState.READY: ReadyState,
            ATMState.CARD_READING: CardReadingState,
            ATMState.WITHDRAWAL_DETAILS_READING: WithdrawalDetailsReadingState,
            ATMState.CASH_DISPENSING: CashDispensingState,
            ATMState.CARD_EJECTING: CardEjectingState,
        }
        return state_classes[atm_state](self)

    def change_state(self, new_state):
        self.state = self.get_state(new_state)
        DBAccessor.update_atm_state(self.machine_id, new_state)