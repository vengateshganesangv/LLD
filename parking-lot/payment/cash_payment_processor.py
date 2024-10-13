from payment.payment_processor import PaymentProcessor

class CashPaymentProcessor(PaymentProcessor):
    def __init__(self, amount: float):
        self.amount = amount

    def execute_payment(self) -> bool:
        return False

    def get_amount(self) -> float:
        return 0  # You might want to change this to
