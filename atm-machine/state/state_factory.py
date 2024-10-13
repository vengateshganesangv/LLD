from state.atm_state import ATMState
from state.ready_state import ReadyState
from state.card_reading_state import CardReadingState
from state.withdrawal_details_reading_state import WithdrawalDetailsReadingState
from state.cash_dispensing_state import CashDispensingState
from state.card_ejecting_state import CardEjectingState

class StateFactory:
    @staticmethod
    def get_state(atm_state, atm):
        if atm_state == ATMState.READY:
            return ReadyState(atm)
        elif atm_state == ATMState.CARD_READING:
            return CardReadingState(atm)
        elif atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            return WithdrawalDetailsReadingState(atm)
        elif atm_state == ATMState.CASH_DISPENSING:
            return CashDispensingState(atm)
        elif atm_state == ATMState.CARD_EJECTING:
            return CardEjectingState(atm)
        else:
            raise ValueError("Invalid state")