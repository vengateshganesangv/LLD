from order_state.order_state import OrderState
from order_state.delivered_state import DeliveredState

class InTransitState(OrderState):
    def schedule_pickup(self, pickup_details: dict):
        self.transition_error("schedule pickup")

    def pickup(self):
        self.transition_error("pickup")

    def deliver(self):
        self.order.set_order_state(DeliveredState(self.order))
        print(f"Order {self.order.id} has been delivered")

    def cancel(self):
        self.transition_error("cancel")

    def get_status(self) -> str:
        return "IN_TRANSIT"