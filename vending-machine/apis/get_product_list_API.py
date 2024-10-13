# api/get_product_list_api.py
from custom_enum.database_name_enum import DatabaseNameEnum
from entity.product_entity import Product
from factory.product_manager_factory import ProductManagerFactory

class GetProductListAPI:
    def get_product_list(self) -> list[Product]:
        product_manager = ProductManagerFactory.get_product_manager(DatabaseNameEnum.INMEMORY)
        return product_manager.get_product_list()