from data.cart import Cart
from data.product import Product
from data.product_copy import ProductCopy
from data.rating import Rating
from data.user import User
from data.order import Order
from data.address import Address

class DBAccessor:
    @staticmethod
    def get_products_by_name(product_name: str) -> list[Product]:
        # Mocked product data
        return [
            Product(1, "Product A", "Description of Product A", 500.0, Rating.FIVE, True),
            Product(2, "Product B", "Description of Product B", 1500.0, Rating.THREE, False),
            Product(3, "Product C", "Description of Product C", 750.0, Rating.FOUR, True),
            Product(4, "Product D", "Description of Product D", 2000.0, Rating.TWO, False),
        ]

    @staticmethod
    def get_product_copy_id(product_id: int) -> ProductCopy:
        # Mocked product copy data
        product = DBAccessor.get_products_by_name("")[0]  # Get the first product as a mock
        return ProductCopy(product, product_id, False)

    @staticmethod
    def get_cart(user: User) -> Cart:
        # Mocked cart data
        return Cart(1)

    @staticmethod
    def persist_cart(cart: Cart, user: User):
        # Mock implementation of persisting cart
        pass

    @staticmethod
    def check_out_cart(user: User):
        # Mock implementation of checking out cart
        pass

    @staticmethod
    def create_order(user: User, cart: Cart) -> int:
        # Mock implementation of creating an order
        return 1

    @staticmethod
    def get_order_by_id(order_id: int) -> Order:
        # Mock implementation of getting an order by ID
        cart = Cart(1)
        shipping_address = Address("123 Main St", "", "", "City", "State", "Country", "12345")
        billing_address = Address("456 Elm St", "", "", "City", "State", "Country", "67890")
        return Order(order_id, cart, shipping_address, billing_address)