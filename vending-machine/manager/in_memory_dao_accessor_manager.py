from db.db import CART_TABLE
from entity.cart_entity import Cart

#Seperate Accessor Layer Needed for Order, Cart and Product. For Now I Keep it simple
class InMemoryDAOAccessor:
    def __init__(self):
        raise RuntimeError("This class should not be instantiated")
    @staticmethod
    def addToCart(transaction_id,product_id,product_quantity, amount):
        newCart = Cart(transaction_id,product_id,product_quantity, amount)
        id = newCart.id
        CART_TABLE[id] = newCart
        return True
    @staticmethod
    def get_cart_info():
        return CART_TABLE.items()