from custom_enum.payment_mode_status_enum import PaymentModeStatusEnum
from dto.cart_info_dto import CartInfoDTO
from dto.payment_repsonse_dto import PaymentResponseDTO
from manager.abstract_cart_manager import AbstractCartManager
from manager.abstract_payment_manager import AbstractPaymentManager

class CashBasedPaymentManager(AbstractPaymentManager):
    def __init__(self, amount):
        self.amount = amount
    def execute_payment(self, payment_response: PaymentResponseDTO) -> PaymentResponseDTO:
        payment_response.payment_mode_status = PaymentModeStatusEnum.SUCCEED
        return payment_response
    def process_payment(self, cart_manager : AbstractCartManager) -> PaymentResponseDTO:
        cart_products : CartInfoDTO = cart_manager.get_cart_info()
        payment_response = self.payment_response_mapper(cart_products.total_amount, self.amount)
        return payment_response
    def process_refund(self, amount: int):
        print(f"Processing debit card refund of ${amount/100:.2f}")
        return True