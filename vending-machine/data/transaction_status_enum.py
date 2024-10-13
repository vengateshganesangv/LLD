from enum import Enum

class TransactionStatusEnum(Enum):
    PROCESSING = "PROCESSING"
    SUCCEED = "SUCCEED"
    FAILED = "FAILED"