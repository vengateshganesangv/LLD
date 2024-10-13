from dao.abstract_dao import AbstractDAO
from db.db import CART_TABLE
from entity.cart_entity import Cart

class CartDAO(AbstractDAO):
    def create(self, cart: Cart):
        CART_TABLE[cart.id] = cart
        return True

    def read(self, id):
        return CART_TABLE.get(id)

    def update(self, cart: Cart):
        if cart.id in CART_TABLE:
            CART_TABLE[cart.id] = cart
            return True
        return False

    def delete(self, id):
        if id in CART_TABLE:
            del CART_TABLE[id]
            return True
        return False

    def get_all(self):
        return list(CART_TABLE.values())