from data.cart import Cart
from data.product_copy import ProductCopy
from data.user import User
from db.db_accessor import DBAccessor


class CartManager:
    def get_cart(self, user: User) -> Cart:
        return DBAccessor.get_cart(user)

    def add_to_cart(self, user: User, product_copy: ProductCopy):
        if product_copy.is_sold():
            raise RuntimeError("Cannot add to cart")
        
        cart = self.get_cart(user)
        cart.add(product_copy)
        DBAccessor.persist_cart(cart, user)

    def remove_from_cart(self, user: User, product_copy: ProductCopy):
        cart = self.get_cart(user)
        cart.remove(product_copy)
        DBAccessor.persist_cart(cart, user)

    def checkout_cart(self, user: User):
        DBAccessor.check_out_cart(user)
