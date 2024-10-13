# order_state/order_placed_state.py
from notification.publisher.order_status_publisher import OrderStatusPublisher
from order_state.order_state import OrderState
from order_state.pickup_scheduled_state import PickupScheduledState

class OrderPlacedState(OrderState):
    def __init__(self, order):
        super().__init__(order)
        self.publisher = OrderStatusPublisher()
    def schedule_pickup(self, pickup_details: dict):
        self.order.set_order_state(PickupScheduledState(self.order))
        print(f"Pickup scheduled for order {self.order.id}")

    def pickup(self):
        self.transition_error("pickup")

    def deliver(self):
        self.transition_error("deliver")

    def cancel(self):
        # Implement cancellation logic
        print(f"Order {self.order.id} has been cancelled")

    def get_status(self) -> str:
        return "ORDER_PLACED"