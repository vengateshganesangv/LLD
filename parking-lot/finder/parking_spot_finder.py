from data.parking_spot import ParkingSpot
from manager.vehicle_type_manager import VehicleTypeManager
from selector.parking_spot_selector import ParkingSpotSelector

class ParkingSpotFinder:
    def __init__(self, vehicle_type_manager: VehicleTypeManager, parking_spot_selector: ParkingSpotSelector):
        self.vehicle_type_manager = vehicle_type_manager
        self.parking_spot_selector = parking_spot_selector

    def find_parking_spot(self) -> ParkingSpot:
        parking_spots = self.vehicle_type_manager.get_parking_spots()
        return self.parking_spot_selector.select_spot(parking_spots)
