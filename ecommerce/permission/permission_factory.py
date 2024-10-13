
from data.product_copy import ProductCopy
from data.user import User
from permission.add_to_cart_permission import AddToCartPermission
from permission.search_permission import SearchProductPermission


class PermissionFactory:
    @staticmethod
    def get_search_permission(user):
        # Simulate querying DB and constructing the permission
        return SearchProductPermission(user)
    @staticmethod
    def get_add_to_cart_permission(user: User, product_copy: ProductCopy):
        return AddToCartPermission(user, product_copy)