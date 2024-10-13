
class Product:
    _next_id = 1
    def __init__(self, name: str, qty_available: int, price: float) -> None:
        self._id = Product._next_id
        Product._next_id += 1
        self._name = name
        self._qty_available = qty_available
        self._price = price
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def qty_available(self) -> int:
        return self._qty_available

    @qty_available.setter
    def qty_available(self, value) -> int:
        self._qty_available = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        self._price = value

    def __repr__(self) -> str:
        return str(self.__dict__)