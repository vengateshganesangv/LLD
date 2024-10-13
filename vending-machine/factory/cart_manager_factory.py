# factory/cart_manager_factory.py
from custom_enum.database_name_enum import DatabaseNameEnum
from manager.abstract_cart_manager import AbstractCartManager
from manager.in_memory_cart_manager import InMemoryCartManager

class CartManagerFactory:
    @staticmethod
    def get_cart_manager(type: DatabaseNameEnum) -> AbstractCartManager:
        if type == DatabaseNameEnum.INMEMORY:
            return InMemoryCartManager()
        raise ValueError(f"Unsupported database type: {type}")