# manager/debit_card_payment_manager.py
from custom_enum.payment_mode_status_enum import PaymentModeStatusEnum
from dto.payment_repsonse_dto import PaymentResponseDTO
from manager.abstract_payment_manager import AbstractPaymentManager
from manager.abstract_cart_manager import AbstractCartManager

class DebitCardPaymentManager(AbstractPaymentManager):
    def __init__(self, card_number: str, expiry_date: str, cvv: str, amount: float):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.amount = amount

    def execute_payment(self, payment_response: PaymentResponseDTO) -> PaymentResponseDTO:
        print(f"Processing debit card payment for amount: ${payment_response.amount_paid/100:.2f}")
        payment_response.payment_mode_status = PaymentModeStatusEnum.SUCCEED
        return payment_response

    def process_payment(self, cart_manager: AbstractCartManager) -> PaymentResponseDTO:
        cart_info = cart_manager.get_cart_info()
        total_amount = cart_info.total_amount
        # In a real scenario, we would process the payment with a payment gateway
        payment_response = self.payment_response_mapper(total_amount, self.amount)
        return payment_response

    def process_refund(self, amount: int):
        print(f"Processing debit card refund of ${amount/100:.2f} to card ending in {self.card_number[-4:]}")
        # In a real scenario, we would process the refund with a payment gateway
        return True