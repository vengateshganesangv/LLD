from card.card_manager import CardManager

class DebitCardManager(CardManager):
    def validate_card(self, card_details):
        # Implement debit card validation logic
        return True

    def validate_withdrawal(self, amount, trans_id):
        # Implement debit card withdrawal validation logic
        return True

    def execute_withdrawal(self, trans_id):
        # Implement debit card withdrawal execution logic
        pass