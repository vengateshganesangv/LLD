from order_state.order_state import OrderState
from order_state.in_transit_state import InTransitState

class PickupScheduledState(OrderState):
    def schedule_pickup(self, pickup_details: dict):
        self.transition_error("schedule pickup")

    def pickup(self):
        self.order.set_order_state(InTransitState(self.order))
        print(f"Order {self.order.id} has been picked up and is in transit")

    def deliver(self):
        self.transition_error("deliver")

    def cancel(self):
        # Implement cancellation logic
        print(f"Order {self.order.id} has been cancelled")

    def get_status(self) -> str:
        return "PICKUP_SCHEDULED"