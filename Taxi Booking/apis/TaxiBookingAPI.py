from data.Customer import Customer
from data.BookingInfo import BookingInfo
from manager.BookingManager import BookingManager

class TaxiBookingAPI:
    def __init__(self):
        self.bookingManager = BookingManager()
    def bookTaxi(self, customer: Customer, bookingInfo: BookingInfo):
        self.bookingManager.bookTaxi(customer, bookingInfo)
