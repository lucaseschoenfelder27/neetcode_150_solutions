class UndergroundSystem(object):

    def __init__(self):
        self.customers = {} #customer[id] = [(stationName, t)]
        self.trip_times = {} #trip_times[startStation][endStation] = [t0, ..., tn]
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.customers[id] = [(stationName, t)]
        if stationName not in self.trip_times:
            self.trip_times[stationName] = {}


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.customers[id].append((stationName, t))
        initialStation = self.customers[id][0][0]
        customer_t1 = self.customers[id][0][1]

        ##trip_times[startStation][endStation] = [t0, ..., tn]
        if stationName not in self.trip_times[initialStation]:
            self.trip_times[initialStation][stationName] = []
        self.trip_times[initialStation][stationName].append(t - customer_t1)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(sum(self.trip_times[startStation][endStation])) / len(self.trip_times[startStation][endStation])

