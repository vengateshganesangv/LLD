from data.payment_status import PaymentStatus

class PaymentResponse:
    def __init__(self, amount: float, payment_id: int, status: PaymentStatus):
        self.amount = amount
        self.id = payment_id
        self.status = status

    def __str__(self):
        return f"Payment ID: {self.id}, Amount: {self.amount}, Status: {self.status.value}"