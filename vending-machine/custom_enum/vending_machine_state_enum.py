from enum import Enum

class VendingMachineStateEnum(Enum):
    READY = "READY"
    PRODUCT_DISPLAY = "PRODUCT_DISPLAY"
    PRODUCT_DETAILS_READING = "PRODUCT_DETAILS_READING"
    CART_SHOW_STATE = "CART_SHOW_STATE"
    PLACE_ORDER = "PLACE_ORDER"
    PAYMENT_DISPENCING = "PAYMENT_DISPENCING"
    PRODUCT_DISPENCING = "PRODUCT_DISPENCING"

