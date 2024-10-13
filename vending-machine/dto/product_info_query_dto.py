class ProductInfoQueryDTO:
    def __init__(self,id: int, quantity: int):
        self._id = id
        self._quantity = quantity

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
