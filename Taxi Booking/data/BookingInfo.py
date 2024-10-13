class BookingInfo:
    def __init__(self, pickupPoint: str, dropPoint: str, pickUpTime: int):
        self._pickupPoint = pickupPoint
        self._dropPoint = dropPoint
        self._pickUpTime = pickUpTime

    @property
    def pickupPoint(self):
        return self._pickupPoint

    @pickupPoint.setter
    def pickupPoint(self, value):
        self._pickupPoint = value

    @property
    def dropPoint(self):
        return self._dropPoint

    @dropPoint.setter
    def dropPoint(self, value):
        self._dropPoint = value

    @property
    def pickUpTime(self):
        return self._pickUpTime

    @pickUpTime.setter
    def pickUpTime(self, value):
        self._pickUpTime = value

    