from data.DatabaseName import DatabaseName
from manager.AbstractProductManager import AbstractProductManager
from manager.InMemoryProductManager import InMemoryProductManager
class ProductManagerFactory:
    def __init__(self):
        raise NotImplementedError("This class should not be instantiated")
    @staticmethod
    def getProductManager(type: DatabaseName) -> AbstractProductManager | None:
        productManager = None
        if (type == DatabaseName.INMEMORY):
            productManager = InMemoryProductManager()
        return productManager
        
