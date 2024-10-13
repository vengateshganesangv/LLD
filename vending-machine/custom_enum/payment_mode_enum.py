from enum import Enum

class PaymentModeEnum(Enum):
    CASH_BASED = "CASH_BASED"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    UPI = "UPI"