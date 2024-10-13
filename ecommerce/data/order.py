from data.address import Address
from data.cart import Cart
from order_state.order_state import OrderState
from order_state.order_placed_state import OrderPlacedState

class Order:
    def __init__(self, order_id: int, cart: Cart, shipping_address: Address, billing_address: Address):
        self.id = order_id
        self.cart = cart
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.order_state: OrderState = OrderPlacedState(self)

    def get_order_state(self) -> OrderState:
        return self.order_state

    def set_order_state(self, order_state: OrderState):
        self.order_state = order_state

    def schedule_pickup(self, pickup_details: dict):
        self.order_state.schedule_pickup(pickup_details)

    def cancel(self):
        self.order_state.cancel()

    def pickup(self):
        self.order_state.pickup()

    def deliver(self):
        self.order_state.deliver()

    def get_status(self):
        return self.order_state.get_status()