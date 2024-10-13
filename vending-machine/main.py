from VendingMachine import VendingMachine
from custom_enum.payment_mode_enum import PaymentModeEnum
from db.db import ORDER_LINE_TABLE
from dto.product_info_query_dto import ProductInfoQueryDTO

DEFAULT_MACHINE_ID = 1
vending_machine = VendingMachine(DEFAULT_MACHINE_ID)
print(f"Vending Machine Current State: {vending_machine.get_state()}")
transactionId = vending_machine.init()
print(f"TransactionId: {transactionId}")
print(f"Vending Machine Current State {vending_machine.get_state()}")
products = vending_machine.show_product_details()
print(f"List Of Products {products}")
added_product_list = [ProductInfoQueryDTO(1,2), ProductInfoQueryDTO(2,2)]
is_success_product_reading = vending_machine.read_product_details(transactionId, added_product_list)
print(f"Is Product detail reading success: {is_success_product_reading}")
print(f"Vending Machine Current State {vending_machine.get_state()}")
cart_Info = vending_machine.show_cart()
print(f"Cart Info: {cart_Info}")
payment_info = {
    "amount": 40
}
order = vending_machine.place_order(payment_info, PaymentModeEnum.CASH_BASED, transactionId)
print(f"Order {order}")
print(f"ORDER LINE ITEMS {ORDER_LINE_TABLE}")


