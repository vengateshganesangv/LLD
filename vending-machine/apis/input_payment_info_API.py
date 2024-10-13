from custom_enum.payment_mode_enum import PaymentModeEnum

class InputPaymentInfoAPI:
    def get_payment_info(self, payment_mode: PaymentModeEnum) -> dict:
        if payment_mode == PaymentModeEnum.CASH_BASED:
            amount = float(input("Enter cash amount: "))
            return {"amount": amount}
        elif payment_mode == PaymentModeEnum.DEBIT_CARD:
            card_number = input("Enter card number: ")
            expiry_date = input("Enter expiry date (MM/YY): ")
            cvv = input("Enter CVV: ")
            amount = float(input("Enter amount: "))
            return {"card_number": card_number, "expiry_date": expiry_date, "cvv": cvv, "amount": amount}
        # Add more payment modes as needed
        else:
            raise ValueError(f"Unsupported payment mode: {payment_mode}")