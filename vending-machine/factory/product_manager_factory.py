from custom_enum.database_name_enum import DatabaseNameEnum
from manager.abstract_product_manager import AbstractProductManager
from manager.in_memory_product_manager import InMemoryProductManager

class ProductManagerFactory:
    @staticmethod
    def get_product_manager(type: DatabaseNameEnum) -> AbstractProductManager:
        if type == DatabaseNameEnum.INMEMORY:
            return InMemoryProductManager()
        raise ValueError(f"Unsupported database type: {type}")