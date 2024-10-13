from manager.card_based_payment_manager import CardBasedPaymentManager
from manager.payment_manager import PaymentManager

class PaymentManagerFactory:
    @staticmethod
    def get_payment_manager(payment_mode: str, payment_info: dict) -> PaymentManager:
        if payment_mode == "CardBased":
            return PaymentManagerFactory.get_card_based_payment_manager(payment_info)
        else:
            raise RuntimeError("Invalid paymentMode")
        
    @staticmethod
    def get_card_based_payment_manager(payment_info: dict) -> PaymentManager:
        return CardBasedPaymentManager(
            payment_info.get("bankName"),
            payment_info.get("cardNumber"),
            payment_info.get("pin"),
            float(payment_info.get("amount"))
        )