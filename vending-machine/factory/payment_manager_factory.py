from custom_enum.payment_mode_enum import PaymentModeEnum
from manager.cash_based_payment_manager import CashBasedPaymentManager
from manager.debit_card_payment_manager import DebitCardPaymentManager
from manager.abstract_payment_manager import AbstractPaymentManager

class PaymentManagerFactory:
    @staticmethod
    def get_payment_manager(payment_mode: PaymentModeEnum, payment_info: dict[str, str]) -> AbstractPaymentManager:
        if payment_mode == PaymentModeEnum.CASH_BASED:
            return CashBasedPaymentManager(float(payment_info["amount"]))
        elif payment_mode == PaymentModeEnum.DEBIT_CARD:
            return DebitCardPaymentManager(payment_info["card_number"], payment_info["expiry_date"], payment_info["cvv"], payment_info["amount"])
        raise ValueError(f"Unsupported payment mode: {payment_mode}")