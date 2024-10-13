# api/get_order_refund_value_api.py
from custom_enum.database_name_enum import DatabaseNameEnum
from factory.order_manager_factory import OrderManagerFactory

class GetOrderRefundValueAPI:
    def get_order_refund_value(self, order_id: int) -> int:
        order_manager = OrderManagerFactory.get_order_manager(DatabaseNameEnum.INMEMORY)
        return order_manager.get_order_refund_value(order_id)