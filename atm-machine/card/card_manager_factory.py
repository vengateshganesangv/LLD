from card.card_type import CardType
from card.debit_card_manager import DebitCardManager
from card.credit_card_manager import CreditCardManager

class CardManagerFactory:
    @staticmethod
    def get_card_manager(card_type):
        if card_type == CardType.DEBIT:
            return DebitCardManager()
        elif card_type == CardType.CREDIT:
            return CreditCardManager()
        else:
            raise ValueError("Invalid card type")