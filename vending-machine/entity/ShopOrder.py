from entity.order_line_entity import OrderLine
class ShopOrder:
    def __init__(self, id: int, purchaser_id: int, order_total: float):
        self._id = id
        self._purchaser_id = purchaser_id
        self._order_total = order_total
        self.order_line : [OrderLine] = [] # type: ignore

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value

    @property
    def order_total(self):
        return self._order_total

    @order_total.setter
    def order_total(self, value):
        self._order_total = value
