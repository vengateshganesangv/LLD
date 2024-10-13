from entity.cart_entity import Cart
from entity.machine_entity import Machine
from entity.product_entity import Product
from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from entity.transaction_entity import Transaction

PRODUCT_TABLE: dict[int, Product] = {
    1: Product('Diary Milk', 5, 5),
    2: Product('water bottle', 10, 20),
    3: Product('Candy Man', 20, 3.5)
}

TRANSACTION_TABLE: dict[int, Transaction] = {}
CART_TABLE: dict[int, Cart] = {}
SHOP_ORDER_TABLE = {}
ORDER_LINE_TABLE = {}
MACHINE_TABLE = {
    1: Machine(VendingMachineStateEnum.READY)
}