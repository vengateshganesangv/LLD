from data.ticket import Ticket
from manager.vehicletype_manager_factory import VehicleTypeManagerFactory
from payment.payment_processor import PaymentProcessor

class ParkingFeeProcessor:
    def get_parking_fees(self, ticket: Ticket) -> float:
        duration = 0  # figure out the duration from ticket.vechicle.entry_time
        return VehicleTypeManagerFactory.get_vehicle_type_manager(ticket.vehicle.vehicle_type).get_parking_fees(duration)

    def process_parking_fees(self, ticket: Ticket, payment_processor: PaymentProcessor) -> bool:
        if self.get_parking_fees(ticket) != payment_processor.get_amount():
            raise ValueError("Payment amount mismatch")
        return payment_processor.execute_payment()
