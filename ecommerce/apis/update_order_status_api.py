from data.order import Order
from manager.order_manager import OrderManager

class UpdateOrderStatusAPI:
    def __init__(self, order_manager: OrderManager):
        self.order_manager = order_manager

    def update_order_status(self, order_id: int, new_status: str, details: dict = None) -> Order:
        order: Order = self.order_manager.get_order(order_id)
        if not order:
            raise ValueError("Invalid order id")
        
        try:
            if new_status == "PICKUP_SCHEDULED":
                order.schedule_pickup(details)
            elif new_status == "IN_TRANSIT":
                order.pickup()
            elif new_status == "DELIVERED":
                order.deliver()
            elif new_status == "CANCELED":
                order.cancel()
            else:
                raise ValueError("Invalid status")
        except ValueError as e:
            print(f"Error updating order status: {str(e)}")
        
        return order