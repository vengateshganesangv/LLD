from abc import ABC, abstractmethod
from custom_enum.payment_mode_status_enum import PaymentModeStatusEnum
from custom_enum.payment_status_enum import PaymentStatusEnum
from dto.payment_repsonse_dto import PaymentResponseDTO
from manager.abstract_cart_manager import AbstractCartManager

class AbstractPaymentManager(ABC):
    @abstractmethod
    def execute_payment(self, payment_response: PaymentResponseDTO) -> PaymentResponseDTO:
        pass

    @abstractmethod
    def process_payment(self, cart_manager: AbstractCartManager) -> PaymentResponseDTO:
        pass

    def payment_response_mapper(self, amount_to_pay: float, amount_added: float) -> PaymentResponseDTO:
        if amount_to_pay < amount_added:
            amount_to_refund = amount_added - amount_to_pay
            return PaymentResponseDTO(PaymentStatusEnum.OVER_PAID, amount_added, amount_to_refund, PaymentModeStatusEnum.PROCESSING)
        elif amount_to_pay > amount_added:
            amount_to_refund = amount_to_pay - amount_added
            return PaymentResponseDTO(PaymentStatusEnum.UNDER_PAID, amount_added, amount_to_refund, PaymentModeStatusEnum.PROCESSING)
        else:
            return PaymentResponseDTO(PaymentStatusEnum.EQUAL, amount_added, 0, PaymentModeStatusEnum.PROCESSING)
    
    @abstractmethod
    def process_refund(self, amount: int):
        pass