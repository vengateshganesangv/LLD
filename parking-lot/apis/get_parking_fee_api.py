from data.ticket import Ticket
from payment.parking_fee_processor import ParkingFeeProcessor

class GetParkingFeeAPI:
    def get_parking_fee(self, ticket: Ticket) -> float:
        return ParkingFeeProcessor().get_parking_fees(ticket)
