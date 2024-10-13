from data.entry_point import EntryPoint
from selector.parking_spot_selector import ParkingSpotSelector
from selector.nearest_selector import NearestSelector
from selector.random_selector import RandomSelector

class SpotSelectorFactory:
    def __init__(self):
        # Private constructor ensures the class cannot be instantiated
        raise NotImplementedError("This class should not be instantiated")

    @staticmethod
    def get_nearest_parking_spot_selector(entry_point: EntryPoint) -> ParkingSpotSelector:
        # NearestSelector SelectSpot Need to know about entry point so we can use this kind of pattern
        return NearestSelector(entry_point)

    @staticmethod
    def get_random_selector() -> ParkingSpotSelector:
        return RandomSelector()
