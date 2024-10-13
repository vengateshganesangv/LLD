from data.entry_point import EntryPoint
from data.parking_spot import ParkingSpot
from selector.parking_spot_selector import ParkingSpotSelector

class NearestSelector(ParkingSpotSelector):
    def __init__(self, entry_point: EntryPoint):
        self.entry_point = entry_point

    def select_spot(self, parking_spots: list[ParkingSpot]) -> ParkingSpot:
        # Actual implementation to select the nearest parking spot based on entry point
        # For now, returning the first spot as an example
        return parking_spots[0] if parking_spots else None
