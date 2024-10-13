from data.DatabaseName import DatabaseName
from factory.ProductManagerFactory import ProductManagerFactory
from manager.AbstractProductManager import AbstractProductManager
from data.ProductInfoQuery import ProductInfoQuery
from manager.AmountProcessingManager import AmountProcessingManager

class GetProductAmountAPI:
    def getProductAmount(self, productDetails: list[ProductInfoQuery]) -> float:
        DATABASE_NAME = DatabaseName.INMEMORY
        productManager: AbstractProductManager 
        productManager = ProductManagerFactory.getProductManager(DATABASE_NAME)
        return AmountProcessingManager().get_product_total_amount(productManager, productDetails)
        