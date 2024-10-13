from data.Customer import Customer
from data.BookingInfo import BookingInfo
from manager.TaxiManager import TaxiManager

class BookingManager:
    def __init__(self):
        self.taxiManager = TaxiManager()

    def bookTaxi(self, customer, bookingInfo):
        isValidEndPoint = self.taxiManager.isValidDroppingPoint(bookingInfo.pickupPoint, bookingInfo.dropPoint)
        if not isValidEndPoint:
            raise Exception("Invalid Endpoints")
        
        nextTaxi = self.taxiManager.getNearestTaxi(bookingInfo.pickupPoint, bookingInfo.pickUpTime)
        if not nextTaxi:
            raise Exception("No Taxi Found")
        
        timeToTravel = self.taxiManager.timeForTravel(bookingInfo.pickupPoint, bookingInfo.dropPoint)
        nextTaxi.nextAvailableTime = timeToTravel + bookingInfo.pickUpTime
        
        totalEarning = self.taxiManager.totalCost(bookingInfo.pickupPoint, bookingInfo.dropPoint)
        nextTaxi.totalEarning += totalEarning
        
        self.taxiManager.bookTaxi(bookingInfo.dropPoint, nextTaxi)


