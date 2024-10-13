from data.vehicle_type import VehicleType
from datetime import datetime

class Vehicle:
    def __init__(self, name: str, vehicle_type: VehicleType, number: str, entry_time: datetime):
        self._name = name
        self._vehicle_type = vehicle_type
        self._number = number
        self._entry_time = entry_time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def entry_time(self):
        return self._entry_time

    @entry_time.setter
    def entry_time(self, value):
        self._entry_time = value


    
