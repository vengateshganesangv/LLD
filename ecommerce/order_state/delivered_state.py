from order_state.order_state import OrderState

class DeliveredState(OrderState):
    def schedule_pickup(self, pickup_details: dict):
        self.transition_error("schedule pickup")

    def pickup(self):
        self.transition_error("pickup")

    def deliver(self):
        self.transition_error("deliver")

    def cancel(self):
        self.transition_error("cancel")

    def get_status(self) -> str:
        return "DELIVERED"