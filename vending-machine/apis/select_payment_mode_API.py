from custom_enum.payment_mode_enum import PaymentModeEnum

class SelectPaymentModeAPI:
    def select_payment_mode(self) -> PaymentModeEnum:
        print("Select payment mode:")
        for mode in PaymentModeEnum:
            print(f"{mode.value}: {mode.name}")
        
        while True:
            choice = input("Enter your choice: ").upper()
            try:
                return PaymentModeEnum(choice)
            except ValueError:
                print("Invalid choice. Please try again.")