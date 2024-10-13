from custom_enum.database_name_enum import DatabaseNameEnum
from dto.cart_info_dto import CartInfoDTO
from factory.cart_manager_factory import CartManagerFactory

class GetCartInfoAPI:
    def get_cart_product_info(self) -> CartInfoDTO:
        cart_manager = CartManagerFactory.get_cart_manager(DatabaseNameEnum.INMEMORY)
        return cart_manager.get_cart_info()