from db.db_accessor import DBAccessor
from factory.filter_factory import FilterFactory


class ProductSearcher:
    def search_products(self, product_name: str, filter_details):
        products = DBAccessor.get_products_by_name(product_name)
        return FilterFactory.get_product_filter(filter_details).filter(products)
