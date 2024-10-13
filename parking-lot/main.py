from data.entry_point import EntryPoint
from data.spot_selection import SpotSelection
from data.vehicle_type import VehicleType
from apis.FindParkingSpotAPI import FindParkingSpotAPI

# Create an instance of EntryPoint (Assuming you have a valid entry point)
entry_point = EntryPoint("Entry Point Name", True)

# Select the vehicle type and spot selection strategy (Assuming you have valid selections)
vehicle_type = VehicleType.TWO_WHEELER
spot_selection = SpotSelection.RANDOM

# Create an instance of FindParkingSpotAPI
find_parking_spot_api = FindParkingSpotAPI()

# Find a parking spot
parking_spot = find_parking_spot_api.find_parking_spot(entry_point, vehicle_type, spot_selection)

# Print the selected parking spot (or do whatever you need with it)
print(f"Selected Parking Spot: {parking_spot.name} on Floor {parking_spot.floor_num}")
