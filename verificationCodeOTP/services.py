from datetime import datetime
class allReusableMethods():
    def timedifference(creationDate, currentDate):
        #d1 = datetime.strptime(creationDate, "%Y-%m-%d %H:%M:%S")
        #d2 = datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S")
        duration = currentDate-creationDate
        return abs(duration.total_seconds())