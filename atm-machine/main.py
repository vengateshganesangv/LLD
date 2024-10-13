from atm.atm import ATM
from card.card_details import CardDetails
from card.card_type import CardType

def main():
    atm = ATM("ATM001")
    
    trans_id = atm.init()
    print(f"Transaction initialized with ID: {trans_id}")

    # Read card
    card_details = CardDetails(CardType.DEBIT, 1234567890, 1234, "John Doe")
    if atm.read_card(card_details):
        print("Card read successfully")

        # Read withdrawal details
        amount = 100.0
        if atm.read_withdrawal_details(card_details, trans_id, amount):
            print("Withdrawal details read successfully")

            # Dispense cash
            dispensed_amount = atm.dispense_cash(trans_id)
            print(f"Dispensed amount: ${dispensed_amount}")

            # Eject card
            atm.eject_card()
            print("Card ejected")
        else:
            print("Withdrawal not approved")
    else:
        print("Card read failed")

if __name__ == "__main__":
    main()