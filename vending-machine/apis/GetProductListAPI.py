from data.DatabaseName import DatabaseName
from factory.ProductManagerFactory import ProductManagerFactory
from manager.AbstractProductManager import AbstractProductManager
class GetProductListAPI:
    def getProductList(self):
        DATABASE_NAME = DatabaseName.INMEMORY
        productManager: AbstractProductManager 
        productManager = ProductManagerFactory.getProductManager(DATABASE_NAME)
        return productManager.getProductList()
        