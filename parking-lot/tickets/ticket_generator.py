from data.parking_spot import ParkingSpot
from data.ticket import Ticket
from data.vehicle import Vehicle
import uuid

class TicketGenerator:
    def generate_ticket(self, vehicle: Vehicle, parking_spot: ParkingSpot) -> Ticket:
        ticket_num = self.get_unique_ticket_num()
        # logic to check if isFree & then park & persist in DB
        # We can use findParkingSpotAPI For to get the parking spot and use the parking spot
        return Ticket(ticket_num, vehicle, parking_spot)

    def get_unique_ticket_num(self) -> str:
        # Replace with actual logic to generate unique ticket numbers
        return str(uuid.uuid4())
