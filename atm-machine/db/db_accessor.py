from state.atm_state import ATMState
from card.card_details import CardDetails
from card.transaction_status import TransactionStatus

class DBAccessor:
    @staticmethod
    def get_atm_state(machine_id):
        return ATMState.READY

    @staticmethod
    def create_new_transaction(machine_id):
        return 1

    @staticmethod
    def update_atm_state(machine_id, state):
        pass

    @staticmethod
    def persist_card_details(card_details, machine_id):
        pass

    @staticmethod
    def disapprove_transaction(machine_id):
        pass

    @staticmethod
    def cancel_transaction(trans_id):
        pass

    @staticmethod
    def persist_with_details(trans_id, amount, status):
        pass

    @staticmethod
    def mark_as_exec(trans_id):
        return 0.0