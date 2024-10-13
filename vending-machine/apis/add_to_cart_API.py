from custom_enum.database_name_enum import DatabaseNameEnum
from dto.product_info_query_dto import ProductInfoQueryDTO
from factory.cart_manager_factory import CartManagerFactory
from factory.product_manager_factory import ProductManagerFactory

class AddToCartAPI:
    def add_to_cart(self, transaction_id: int, product_details: list[ProductInfoQueryDTO]) -> bool:
        cart_manager = CartManagerFactory.get_cart_manager(DatabaseNameEnum.INMEMORY)
        product_manager = ProductManagerFactory.get_product_manager(DatabaseNameEnum.INMEMORY)
        return cart_manager.add_to_cart(transaction_id, product_details, product_manager)