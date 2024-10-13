from abc import ABC, abstractmethod
from data.parking_spot import ParkingSpot

class VehicleTypeManager(ABC):
    @abstractmethod
    def get_parking_spots(self) -> list[ParkingSpot]:
        pass

    @abstractmethod
    def get_parking_fees(self, duration_in_hours: int) -> float:
        pass
