import random
from data.parking_spot import ParkingSpot
from selector.parking_spot_selector import ParkingSpotSelector

class RandomSelector(ParkingSpotSelector):
    def select_spot(self, parking_spots: list[ParkingSpot]) -> ParkingSpot:
        # Randomly select a parking spot from the list
        return random.choice(parking_spots) if parking_spots else None
