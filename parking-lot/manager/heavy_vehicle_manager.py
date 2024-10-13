from manager.vehicle_type_manager import VehicleTypeManager
from data.parking_spot import ParkingSpot

class HeavyVehicleManager(VehicleTypeManager):
    def get_parking_spots(self) -> list[ParkingSpot]:
        # Actual implementation to fetch parking spots for heavy vehicles
        # For now, returning dummy data
        return [
            ParkingSpot("1", "HEAVY", "Spot1", True),
            ParkingSpot("1", "HEAVY", "Spot2", False),
            ParkingSpot("1", "HEAVY", "Spot3", True),
        ]

    def get_parking_fees(self, duration_in_hours: int) -> float:
        # Actual implementation to calculate parking fees for heavy vehicles
        # For now, returning a fixed value
        return duration_in_hours * 20.0  # Assuming $20 per hour
