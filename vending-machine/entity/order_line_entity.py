class OrderLine:
    _next_id = 1
    def __init__(self, product_id: int, shop_order_id: int, price: float, qty: int) -> None:
        self._id = OrderLine._next_id
        OrderLine._next_id += 1
        self._product_id = product_id
        self._shop_order_id = shop_order_id
        self._price = price
        self._qty = qty
    
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
    def shop_order_id(self) -> int:
        return self._shop_order_id

    @shop_order_id.setter
    def shop_order_id(self, value) -> None:
        self._shop_order_id = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        self._price = value

    @property
    def qty(self) -> int:
        return self._qty

    @qty.setter
    def qty(self, value) -> int:
        self._qty = value
    
    def __repr__(self) -> str:
        return str(self.__dict__)
