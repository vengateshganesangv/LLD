from enum import Enum

# OrderStatus Enum
class OrderStatus(Enum):
    ORDER_PLACED = "Order Placed"
    COOKING = "Cooking"
    READY_FOR_DELIVERY = "Ready for Delivery"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"
