from enum import Enum

class PaymentStatusEnum(Enum):
    OVER_PAID = "OVER_PAID"
    UNDER_PAID = "UNDER_PAID"
    EQUAL = "EQUAL"