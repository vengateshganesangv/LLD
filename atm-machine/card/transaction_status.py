from enum import Enum

class TransactionStatus(Enum):
    APPROVED = 1
    NOT_APPROVED = 2
    EXECUTED = 3
    CANCELED = 4