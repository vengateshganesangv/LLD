from card.card_type import CardType

class CardDetails:
    def __init__(self, card_type: CardType, card_number: int, pin: int, name: str):
        self.card_type = card_type
        self.card_number = card_number
        self.pin = pin
        self.name = name

    def get_card_type(self):
        return self.card_type

    def get_card_number(self):
        return self.card_number

    def get_pin(self):
        return self.pin

    def get_name(self):
        return self.name