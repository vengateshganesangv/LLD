# data/payment_status.py
from enum import Enum

class PaymentStatus(Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'