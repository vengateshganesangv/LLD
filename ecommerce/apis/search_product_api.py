# api/search_product_api.py
from data.filter_details import FilterDetails
from data.product import Product
from data.user import User
from permission.permission_factory import PermissionFactory
from searcher.product_searcher import ProductSearcher

class SearchProductAPI:
    def __init__(self, product_searcher: ProductSearcher):
        self.product_searcher = product_searcher

    def search(self, product_name: str, filter_details: FilterDetails, user: User) -> list[Product]:
        # Functionality whether User Has Permission to search or not To Perform Search Option
        permission = PermissionFactory().get_search_permission(user)
        if not permission.is_permitted():
            raise RuntimeError("Request not allowed")
        return self.product_searcher.search_products(product_name, filter_details)