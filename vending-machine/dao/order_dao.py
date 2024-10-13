from dao.abstract_dao import AbstractDAO
from db.db import SHOP_ORDER_TABLE, ORDER_LINE_TABLE
from entity.shop_order import ShopOrder
from entity.order_line_entity import OrderLine

class OrderDAO(AbstractDAO):
    def create(self, order: ShopOrder):
        SHOP_ORDER_TABLE[order.id] = order
        return True

    def read(self, id):
        return SHOP_ORDER_TABLE.get(id)

    def update(self, order: ShopOrder):
        if order.id in SHOP_ORDER_TABLE:
            SHOP_ORDER_TABLE[order.id] = order
            return True
        return False

    def delete(self, id):
        if id in SHOP_ORDER_TABLE:
            del SHOP_ORDER_TABLE[id]
            return True
        return False

    def create_order_line(self, order_line: OrderLine):
        ORDER_LINE_TABLE[order_line.id] = order_line
        return True

    def get_order_lines(self, order_id):
        return [ol for ol in ORDER_LINE_TABLE.values() if ol.shop_order_id == order_id]