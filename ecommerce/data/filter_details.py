from data.rating import Rating

class FilterDetails:
    def __init__(self, price_filter: float = None, rating_filter: Rating = None, pay_on_del_filter: bool = None):
        self.price_filter = price_filter
        self.rating_filter = rating_filter
        self.pay_on_del_filter = pay_on_del_filter