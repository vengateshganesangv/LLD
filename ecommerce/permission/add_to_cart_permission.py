from data.cart import Cart
from data.product_copy import ProductCopy
from data.user import User
from db.db_accessor import DBAccessor
from permission.permission import Permission


class AddToCartPermission(Permission):
    MAX_CART_AMOUNT = 1_000_000
    DISTINCT_ITEMS_LIMIT = 50
    TOTAL_ITEMS_LIMIT = 1000

    def __init__(self, user: User, product_copy: ProductCopy):
        self.user = user
        self.product_copy = product_copy

    def is_permitted(self) -> bool:
        cart: Cart = DBAccessor.get_cart(self.user)
        return not (
            cart.get_cart_amount() > self.MAX_CART_AMOUNT or
            cart.get_distinct_items_count() > self.DISTINCT_ITEMS_LIMIT or
            cart.get_total_items_count() > self.TOTAL_ITEMS_LIMIT
        )
