from payment.payment_processor import PaymentProcessor
from data.card_details import CardDetails

class CardPaymentProcessor(PaymentProcessor):
    def __init__(self, amount: float, card_details: CardDetails):
        self.amount = amount
        self.card_details = card_details

    def execute_payment(self) -> bool:
        return False

    def get_amount(self) -> float:
        return 0 
