from manager.vehicle_type_manager import VehicleTypeManager
from data.parking_spot import ParkingSpot

class TwoWheelerManager(VehicleTypeManager):
    def get_parking_spots(self) -> list[ParkingSpot]:
        # Actual implementation to fetch parking spots for two-wheelers
        # For now, returning dummy data
        return [
            ParkingSpot("1", "TWO_WHEELER", "Spot1", True),
            ParkingSpot("1", "TWO_WHEELER", "Spot2", False),
            ParkingSpot("1", "TWO_WHEELER", "Spot3", True),
        ]

    def get_parking_fees(self, duration_in_hours: int) -> float:
        # Actual implementation to calculate parking fees for two-wheelers
        # For now, returning a fixed value
        return duration_in_hours * 5.0  # Assuming $5 per hour
