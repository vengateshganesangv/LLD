
from card.card_manager import CardManager

class CreditCardManager(CardManager):
    def validate_card(self, card_details):
        # Implement credit card validation logic
        return True

    def validate_withdrawal(self, amount, trans_id):
        # Implement credit card withdrawal validation logic
        return True

    def execute_withdrawal(self, trans_id):
        # Implement credit card withdrawal execution logic
        pass
