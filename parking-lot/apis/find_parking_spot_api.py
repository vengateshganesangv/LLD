from data.entry_point import EntryPoint
from data.spot_selection import SpotSelection
from data.vehicle_type import VehicleType
from data.parking_spot import ParkingSpot
from manager.vehicle_type_manager import VehicleTypeManager
from manager.vehicletype_manager_factory import VehicleTypeManagerFactory
from selector.spot_selector_factory import SpotSelectorFactory
from finder.parking_spot_finder import ParkingSpotFinder

class FindParkingSpotAPI:
    def find_parking_spot(self, entry_point: EntryPoint, vehicle_type: VehicleType, spot_selection: SpotSelection) -> ParkingSpot:
        # VehicleTypeManager Responsible For Getting list of parking spot + cost for the vehicle
        vehicle_type_manager: VehicleTypeManager = VehicleTypeManagerFactory.get_vehicle_type_manager(vehicle_type)
        # Responsible for selecting parking spot
        parking_spot_selector = None

        if spot_selection == SpotSelection.RANDOM:
            parking_spot_selector = SpotSelectorFactory.get_random_selector()
        elif spot_selection == SpotSelection.NEAREST:
            parking_spot_selector = SpotSelectorFactory.get_nearest_parking_spot_selector(entry_point)
        else:
            raise ValueError("Invalid spot selection")

        return ParkingSpotFinder(vehicle_type_manager, parking_spot_selector).find_parking_spot()
