from data.ProductInfoQuery import ProductInfoQuery
from manager.AbstractProductManager import AbstractProductManager

class AmountProcessingManager:
    def get_product_total_amount(self, productManager: AbstractProductManager, productDetails: list[ProductInfoQuery]) -> float:
        total_amount = 0
        for productInfo in productDetails:
            total_amount += productManager.getProductAmount(productInfo)
        return total_amount
