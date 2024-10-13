from entity.order_line_entity import OrderLine
class ShopOrder:
    _next_id = 1
    def __init__(self, transaction_id: int, order_total: float, amount_added: float, amount_to_refund: float):
        self._id = ShopOrder._next_id
        ShopOrder._next_id += 1
        self._transaction_id = transaction_id
        self._order_total = order_total
        self._amount_added = amount_added
        self._amount_to_refund = amount_to_refund

    @property
    def amount_added(self):
        return self._amount_added

    @amount_added.setter
    def amount_added(self, value):
        self._amount_added = value

    @property
    def amount_to_refund(self):
        return self._amount_to_refund

    @amount_to_refund.setter
    def amount_to_refund(self, value):
        self._amount_to_refund = value

    @property
    def id(self):
        return self._id

    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @property
    def order_total(self):
        return self._order_total

    @order_total.setter
    def order_total(self, value):
        self._order_total = value

    def __repr__(self) -> str:
        return str(self.__dict__)
