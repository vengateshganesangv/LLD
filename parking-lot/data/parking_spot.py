from data.vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, floor_num: str, vehicle_type: VehicleType, name: str, is_free: bool):
        self._floor_num = floor_num
        self._vehicle_type = vehicle_type
        self._name = name
        self._is_free = is_free

    @property
    def floor_num(self) -> str:
        return self._floor_num

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_free(self) -> bool:
        return self._is_free