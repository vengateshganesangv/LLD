from data.db import *
from data.Taxi import Taxi

class TaxiManager:

    def isValidDroppingPoint(self, srcPoint, dstPoint):
        return ord('A') <= ord(srcPoint) <= ord('F') and ord('A') <= ord(dstPoint) <= ord('F')

    def defaultTaxiAssignment(self, n):
        for i in range(1, n+1):
            ENDPOINT_TAXI_INFO['A'].append(Taxi(i))

    def checkUntilValidTaxiFound(self, taxis, pickupTime):
        for i in range(len(taxis)):
            if taxis[i].nextAvailableTime <= pickupTime:
                return taxis.pop(i)
        return False

    def getNearestTaxi(self, srcPoint, pickupTime):
        if len(ENDPOINT_TAXI_INFO[srcPoint]) > 0:
            validTaxi = self.checkUntilValidTaxiFound(list(ENDPOINT_TAXI_INFO[srcPoint]), pickupTime)
            if validTaxi:
                return validTaxi
        curr_pos = ord(srcPoint)
        i = curr_pos - 1
        j = curr_pos + 1
        leftSideTaxi = None
        rightSideTaxi = None
        while i >= ord('A'):
            if len(ENDPOINT_TAXI_INFO[chr(i)]) > 0:
                leftSideTaxi = self.checkUntilValidTaxiFound(list(ENDPOINT_TAXI_INFO[chr(i)]), pickupTime)
                if leftSideTaxi:
                    break
            i -= 1
        while j <= ord('F'):
            if len(ENDPOINT_TAXI_INFO[chr(j)]) > 0:
                rightSideTaxi = self.checkUntilValidTaxiFound(list(ENDPOINT_TAXI_INFO[chr(j)]), pickupTime)
                if rightSideTaxi:
                    break
            j += 1
        if i < ord('A') and j > ord('F'):
            return None
        elif i >= ord('A') and j > ord('F'):
            return leftSideTaxi
        elif i < ord('A') and j <= ord('F'):
            return rightSideTaxi
        else:
            if leftSideTaxi.totalEarning > rightSideTaxi.totalEarning:
                return rightSideTaxi
            else:
                return leftSideTaxi

    def timeForTravel(self, srcPoint, dstPoint):
        timePerEndPoint = 1
        timeFromSrcToDst = timePerEndPoint * abs(ord(srcPoint) - ord(dstPoint))
        return timeFromSrcToDst

    def totalCost(self, srcPoint, dstPoint):
        costForFirstFiveKilometer = 100
        costForSubsequentTravel = 10
        totalDistanceTravel = abs(ord(srcPoint) - ord(dstPoint))
        totalKMTravel = 15 * totalDistanceTravel
        costForFirst = 5 * costForFirstFiveKilometer
        costForSecond = (totalKMTravel - 5) * costForSubsequentTravel
        return costForFirst + costForSecond

    def bookTaxi(self, dstPoint, taxi):
        ENDPOINT_TAXI_INFO[dstPoint].append(taxi)