from payment.payment_processor import PaymentProcessor
from data.card_details import CardDetails
from payment.card_payment_processor import CardPaymentProcessor
from payment.cash_payment_processor import CashPaymentProcessor

class PaymentProcessorFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_card_based_payment_processor(amount: float, card_details: CardDetails) -> PaymentProcessor:
        return CardPaymentProcessor(amount, card_details)

    @staticmethod
    def get_cash_based_payment_processor(amount: float) -> PaymentProcessor:
        return CashPaymentProcessor(amount)
