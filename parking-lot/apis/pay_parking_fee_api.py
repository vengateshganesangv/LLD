from data.ticket import Ticket
from data.card_details import CardDetails
from payment.parking_fee_processor import ParkingFeeProcessor
from data.payment_mode import PaymentMode
from payment.payment_processor_factory import PaymentProcessorFactory

class PayParkingFeesAPI:
    def pay_parking_fee(self, ticket: Ticket, payment_mode: PaymentMode, payment_details: dict) -> bool:
        payment_processor = None

        if payment_mode == PaymentMode.CARD:
            amount = float(payment_details.get("AMOUNT", 0))
            card_details = None  # logic to create the CardDetails object
            payment_processor = PaymentProcessorFactory.get_card_based_payment_processor(amount, card_details)
        elif payment_mode == PaymentMode.CASH:
            amount = float(payment_details.get("AMOUNT", 0))
            payment_processor = PaymentProcessorFactory.get_cash_based_payment_processor(amount)
        else:
            raise ValueError("Invalid Payment Mode")

        return ParkingFeeProcessor().process_parking_fees(ticket, payment_processor)
