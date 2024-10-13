from custom_enum.transaction_status_enum import TransactionStatusEnum


class Transaction:
    _next_id = 1
    def __init__(self, state: TransactionStatusEnum) -> None:
        self._id = Transaction._next_id
        Transaction._next_id += 1
        self._state = state

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value