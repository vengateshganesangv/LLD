class Cart:
    _next_id = 1
    def __init__(self, _transaction_id: int, product_id: int, qty: int, price: float) -> None:
        self._id = Cart._next_id
        Cart._next_id += 1
        self._product_id = product_id
        self._transaction_id = _transaction_id
        self._qty = qty
        self._price = price

    @property
    def id(self) -> int:
        return self._id

    @property
    def product_id(self) -> int:
        return self._product_id

    @product_id.setter
    def product_id(self, value) -> None:
        self._product_id = value

    @property
    def transaction_id(self) -> int:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value) -> None:
        self._transaction_id = value

    @property
    def qty(self) -> int:
        return self._qty

    @qty.setter
    def qty(self, value) -> None:
        self._qty = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> float:
        self._price = value

    def __repr__(self) -> str:
        return str(self.__dict__)