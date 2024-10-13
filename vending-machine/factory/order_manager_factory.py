from custom_enum.database_name_enum import DatabaseNameEnum
from manager.abstract_order_manager import AbstractOrderManager
from manager.in_memory_order_manager import InMemoryOrderManager

class OrderManagerFactory:
    @staticmethod
    def get_order_manager(type: DatabaseNameEnum) -> AbstractOrderManager:
        if type == DatabaseNameEnum.INMEMORY:
            return InMemoryOrderManager()
        raise ValueError(f"Unsupported database type: {type}")