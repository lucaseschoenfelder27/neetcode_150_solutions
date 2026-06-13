import heapq

class StockPrice(object):

    def __init__(self):
        self.records = {}
        self.latest = [0, None]
        self.minhp = []
        self.maxhp = []
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.records[timestamp] = price
        
        if timestamp > self.latest[0]:
            self.latest[0] = timestamp
            self.latest[1] = price
        
        heapq.heappush(self.maxhp, (-price, timestamp, self.records[timestamp]))
        heapq.heappush(self.minhp, (price, timestamp, self.records[timestamp]))

    def current(self):
        """
        :rtype: int
        """
        return self.latest[1]
        

    def maximum(self):
        """
        :rtype: int
        """
        #return max(self.records.values())
        while self.records[self.maxhp[0][1]] != self.maxhp[0][2] and self.maxhp:
            heapq.heappop(self.maxhp)
        return -self.maxhp[0][0] if self.maxhp else None

    def minimum(self):
        """
        :rtype: int
        """
        #return min(self.records.values())
        while self.records[self.minhp[0][1]] != self.minhp[0][2] and self.minhp:
            heapq.heappop(self.minhp)
        return self.minhp[0][0] if self.minhp else None