from data.payment_response import PaymentResponse
from payment_manager import PaymentManager

class CardBasedPaymentManager(PaymentManager):

    def __init__(self, bank_name: str, card_number: str, pin: str, amount: float):
        self.bank_name = bank_name
        self.card_number = card_number
        self.pin = pin
        self.amount = amount

    def execute_payment(self):
        return PaymentResponse("Success", "Card-based payment processed successfully")
