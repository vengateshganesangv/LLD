# api/get_order_items_api.py
from custom_enum.database_name_enum import DatabaseNameEnum
from factory.order_manager_factory import OrderManagerFactory

class GetOrderItemsAPI:
    def get_order_items(self, order_id: int):
        order_manager = OrderManagerFactory.get_order_manager(DatabaseNameEnum.INMEMORY)
        return order_manager.get_order_items(order_id)