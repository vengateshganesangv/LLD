from custom_enum.payment_status_enum import PaymentStatusEnum


class PaymentResponseDTO:
    def __init__(self, payment_status: PaymentStatusEnum, amount_paid : float, amount_to_refund: float, payment_mode_status) -> None:
        self._payment_status = payment_status
        self._amount_paid = amount_paid
        self._amount_to_refund = amount_to_refund
        self._payment_mode_status = payment_mode_status

    @property
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, value):
        self._payment_status = value

    @property
    def amount_paid(self):
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, value):
        self._amount_paid = value

    @property
    def amount_to_refund(self):
        return self._amount_to_refund

    @amount_to_refund.setter
    def amount_to_refund(self, value):
        self._amount_to_refund = value

    @property
    def payment_mode_status(self):
        return self._payment_mode_status

    @payment_mode_status.setter
    def payment_mode_status(self, value):
        self._payment_mode_status = value
