from data.vehicle import Vehicle
from data.parking_spot import ParkingSpot

class Ticket:
    def __init__(self, ref_num: str, vehicle: Vehicle, parking_spot: ParkingSpot):
        self._ref_num = ref_num
        self._vehicle = vehicle
        self._parking_spot = parking_spot

    @property
    def ref_num(self) -> str:
        return self._ref_num

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def parking_spot(self) -> ParkingSpot:
        return self._parking_spot
