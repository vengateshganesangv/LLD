class Taxi:
    def __init__(self, id: int, pickupPoint = 'A', nextAvailableTime = 6, totalEarning = 0, isAvailable = True):
        self._id = id
        self._pickupPoint = pickupPoint
        self._nextAvailableTime = nextAvailableTime
        self._totalEarning = totalEarning
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def pickupPoint(self):
        return self._pickupPoint

    @pickupPoint.setter
    def pickupPoint(self, value):
        self._pickupPoint = value

    @property
    def nextAvailableTime(self):
        return self._nextAvailableTime

    @nextAvailableTime.setter
    def nextAvailableTime(self, value):
        self._nextAvailableTime = value

    @property
    def totalEarning(self):
        return self._totalEarning

    @totalEarning.setter
    def totalEarning(self, value):
        self._totalEarning = value
        
    def __str__(self):
        return f"ID: {self._id}, PickupPoint: {self._pickupPoint}, TotalEarning: {self._totalEarning}, NextAvailableTime: {self._nextAvailableTime}"