from data.rating import Rating

class Product:
    def __init__(self, id: int, name: str, description: str, price_in_inr: float, rating: Rating, is_pay_on_delivery: bool):
        self.id = id
        self.name = name
        self.description = description
        self.price_in_inr = price_in_inr
        self.rating = rating
        self.is_pay_on_delivery = is_pay_on_delivery