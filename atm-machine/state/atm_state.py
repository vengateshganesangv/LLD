from enum import Enum

class ATMState(Enum):
    READY = 1
    CARD_READING = 2
    WITHDRAWAL_DETAILS_READING = 3
    CASH_DISPENSING = 4
    CARD_EJECTING = 5