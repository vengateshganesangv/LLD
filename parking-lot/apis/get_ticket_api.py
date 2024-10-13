from data.parking_spot import ParkingSpot
from data.ticket import Ticket
from data.vehicle import Vehicle
from tickets.ticket_generator import TicketGenerator

class GetTicketAPI:
    def get_ticket(self, vehicle: Vehicle, parking_spot: ParkingSpot) -> Ticket:
        return TicketGenerator().generate_ticket(vehicle, parking_spot)
