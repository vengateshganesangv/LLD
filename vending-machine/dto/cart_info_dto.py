from entity.cart_entity import Cart

class CartInfoDTO:
    def __init__(self, products: list[Cart], total_amount: int):
        self._products = products
        self._total_amount = total_amount

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def __repr__(self) -> str:
        return str(self.__dict__)