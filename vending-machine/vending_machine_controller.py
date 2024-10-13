from enum import Enum
from typing import List

from apis.get_product_list_API import GetProductListAPI
from apis.add_to_cart_API import AddToCartAPI
from apis.get_cart_info_API import GetCartInfoAPI
from apis.place_order_API import PlaceOrderAPI
from apis.get_order_refund_value_API import GetOrderRefundValueAPI
from apis.select_payment_mode_API import SelectPaymentModeAPI
from apis.input_payment_info_API import InputPaymentInfoAPI
from custom_enum.payment_mode_enum import PaymentModeEnum
from dto.product_info_query_dto import ProductInfoQueryDTO
from entity.product_entity import Product
from entity.shop_order import ShopOrder
from factory.payment_manager_factory import PaymentManagerFactory

class OrderMode(Enum):
    ONLINE = "ONLINE"
    PHYSICAL = "PHYSICAL"

class VendingMachineController:
    def __init__(self):
        self.get_product_list_api = GetProductListAPI()
        self.add_to_cart_api = AddToCartAPI()
        self.get_cart_info_api = GetCartInfoAPI()
        self.place_order_api = PlaceOrderAPI()
        self.get_order_refund_value_api = GetOrderRefundValueAPI()
        self.select_payment_mode_api = SelectPaymentModeAPI()
        self.input_payment_info_api = InputPaymentInfoAPI()

    def display_products(self) -> List[Product]:
        return self.get_product_list_api.get_product_list()

    def add_to_cart(self, transaction_id: int, products: List[ProductInfoQueryDTO]) -> bool:
        return self.add_to_cart_api.add_to_cart(transaction_id, products)

    def view_cart(self):
        return self.get_cart_info_api.get_cart_product_info()

    def select_payment_mode(self) -> PaymentModeEnum:
        return self.select_payment_mode_api.select_payment_mode()

    def input_payment_info(self, payment_mode: PaymentModeEnum) -> dict:
        return self.input_payment_info_api.get_payment_info(payment_mode)

    def place_order(self, payment_info: dict, payment_mode: PaymentModeEnum, transaction_id: int) -> ShopOrder:
        return self.place_order_api.place_order(payment_info, payment_mode, transaction_id)

    def get_refund_amount(self, order_id: int) -> int:
        return self.get_order_refund_value_api.get_order_refund_value(order_id)

    def process_refund(self, order_id: int, order_mode: OrderMode, payment_mode: PaymentModeEnum, payment_info: dict):
        refund_amount = self.get_refund_amount(order_id)
        if order_mode == OrderMode.ONLINE:
            self.process_online_refund(refund_amount, payment_mode, payment_info)
        else:
            self.process_physical_refund(refund_amount, payment_mode, payment_info)

    def process_online_refund(self, amount: int, payment_mode: PaymentModeEnum, payment_info: dict):
        payment_manager = PaymentManagerFactory.get_payment_manager(payment_mode, payment_info)
        payment_manager.process_refund(amount)

    def process_physical_refund(self, amount: int, payment_mode: PaymentModeEnum, payment_info: dict):
        if payment_mode == PaymentModeEnum.CASH_BASED:
            print(f"Dispensing physical cash refund of ${amount/100:.2f}")
        else:
            self.process_online_refund(amount, payment_mode, payment_info)

def main():
    controller = VendingMachineController()
    transaction_id = 1  # In a real scenario, this would be generated uniquely

    # Display products
    products = controller.display_products()
    print("Available Products:")
    for product in products:
        print(f"{product.id}: {product.name} - ${product.price/100:.2f} (Available: {product.qty_available})")

    # Simulate user adding products to cart
    selected_products = []
    while True:
        try:
            product_id = int(input("Enter product ID (0 to finish): "))
            if product_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            selected_products.append(ProductInfoQueryDTO(product_id, quantity))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    try:
        controller.add_to_cart(transaction_id, selected_products)
    except ValueError as e:
        print(f"Error adding to cart: {str(e)}")
        return

    # View cart
    cart_info = controller.view_cart()
    print("\nCart Contents:")
    for item in cart_info.products:
        print(f"Product ID: {item.product_id}, Quantity: {item.qty}, Price: ${item.price/100:.2f}")
    print(f"Total: ${cart_info.total_amount/100:.2f}. \n")

    # Select payment mode
    payment_mode = controller.select_payment_mode()

    # Input payment information
    payment_info = controller.input_payment_info(payment_mode)

    # Place order
    order_mode = OrderMode.ONLINE  # In a real scenario, this would be determined based on the user's context

    try:
        order = controller.place_order(payment_info, payment_mode, transaction_id)
        print(f"\nOrder placed successfully. Order ID: {order.id}")

        # Process refund
        controller.process_refund(order.id, order_mode, payment_mode, payment_info)
    except ValueError as e:
        print(f"Error placing order: {str(e)}")

if __name__ == "__main__":
    main()