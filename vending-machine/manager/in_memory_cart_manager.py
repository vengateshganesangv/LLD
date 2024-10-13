from db.db import CART_TABLE
from dto.cart_info_dto import CartInfoDTO
from dto.product_info_query_dto import ProductInfoQueryDTO
from entity.cart_entity import Cart
from manager.abstract_cart_manager import AbstractCartManager
from manager.abstract_product_manager import AbstractProductManager
from manager.in_memory_dao_accessor_manager import InMemoryDAOAccessor

class InMemoryCartManager(AbstractCartManager):
    def __init__(self) -> None:
        super().__init__()
    def add_to_cart(self, transaction_id: int, product_details: list[ProductInfoQueryDTO], product_manager: AbstractProductManager) -> bool:
        totalAmount = 0
        for product in product_details:
            amount = product_manager.get_product_amount(product)
            totalAmount += amount
            #same like this need to be extensible
            InMemoryDAOAccessor.addToCart(transaction_id,product.id,product.quantity, amount)
        return True
    def get_cart_info(self) -> CartInfoDTO:
        product_info : list[Cart] = [] 
        total_amount = 0
        for key, value in InMemoryDAOAccessor.get_cart_info():
            cart: Cart = value
            product_info.append(cart)
            total_amount += cart.price
        cart_info: CartInfoDTO = CartInfoDTO(product_info,total_amount)
        return cart_info
