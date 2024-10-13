from data.vehicle_type import VehicleType
from manager.vehicle_type_manager import VehicleTypeManager
from manager.two_wheeler_manager import TwoWheelerManager
from manager.four_wheeler_manager import FourWheelerManager
from manager.heavy_vehicle_manager import HeavyVehicleManager

class VehicleTypeManagerFactory:
    def __init__(self):
        # Ensures this class isn't instantiated
        raise NotImplementedError("This class should not be instantiated")

    @staticmethod
    def get_vehicle_type_manager(vehicle_type: VehicleType) -> VehicleTypeManager:
        vehicle_type_manager = None

        if vehicle_type == VehicleType.TWO_WHEELER:
            vehicle_type_manager = TwoWheelerManager()
        elif vehicle_type == VehicleType.FOUR_WHEELER:
            vehicle_type_manager = FourWheelerManager()
        elif vehicle_type == VehicleType.HEAVY:
            vehicle_type_manager = HeavyVehicleManager()
        else:
            raise ValueError("Invalid vehicle type")

        return vehicle_type_manager
