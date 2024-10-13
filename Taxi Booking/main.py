from manager.TaxiManager import TaxiManager
from data.Customer import Customer
from data.BookingInfo import BookingInfo
from apis.TaxiBookingAPI import TaxiBookingAPI
def main():
    id = 1
    TaxiManager().defaultTaxiAssignment(4);
    taxiBookingAPI = TaxiBookingAPI()
    while True:
        print("0 -> Book Taxi")
        print("1 -> Print Taxi details")
        choice = int(input())

        if choice == 0:
            customer_id = id
            pickup_point = input("Enter Pickup point: ")
            drop_point = input("Enter Drop point: ")
            pickup_time = int(input("Enter Pickup time: "))
            customerInfo = Customer(customer_id)
            bookingInfo = BookingInfo(pickup_point,drop_point,pickup_time)
            try:
                taxiBookingAPI.bookTaxi(customerInfo,bookingInfo)
            except Exception as e:
                print("Error: " + str(e))
                continue
            id += 1
        else:
            return

if __name__ == "__main__":
    main()