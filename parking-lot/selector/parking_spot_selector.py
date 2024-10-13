from abc import ABC, abstractmethod
from data.parking_spot import ParkingSpot

class ParkingSpotSelector(ABC):
    @abstractmethod
    def select_spot(self, parking_spots: list[ParkingSpot]) -> ParkingSpot:
        pass
