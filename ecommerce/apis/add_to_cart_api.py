# api/add_to_cart_api.py
from data.user import User
from db.db_accessor import DBAccessor
from manager.cart_manager import CartManager
from permission.permission_factory import PermissionFactory

class AddToCartAPI:
    def __init__(self, cart_manager: CartManager):
        self.cart_manager = cart_manager

    def add_to_cart(self, product_id: int, user: User):
        product_copy = DBAccessor.get_product_copy_id(product_id)
        if product_copy is None:
            raise ValueError("Invalid product id")
        
        permission = PermissionFactory.get_add_to_cart_permission(user, product_copy)
        
        if not permission.is_permitted():
            raise PermissionError("Action not allowed")
        
        self.cart_manager.add_to_cart(user, product_copy)