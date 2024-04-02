'''
    Problem: https://leetcode.com/problems/stock-price-fluctuation/
    Concepts: Heap, min max heap
    performance: 35.45% runtime, 24.66% memory
    #todo: improve runtime
'''
import heapq
class StockPrice:

    def __init__(self):
        self.minPrices = []
        self.maxPrices = []
        heapq.heapify(self.minPrices)
        heapq.heapify(self.maxPrices)
        self.pricesDict = dict()
        self.latestTimestamp = 0
        # obselete
        self.curMinTimestamp = None
        self.curMaxTimestamp = None

    def update(self, timestamp: int, price: int) -> None:
        self.pricesDict[timestamp] = price
        self.latestTimestamp = max(self.latestTimestamp, timestamp)
        heapq.heappush(self.minPrices, (price, timestamp))
        heapq.heappush(self.maxPrices, (-price, timestamp))
        
    def current(self) -> int:
        return self.pricesDict[self.latestTimestamp]

    def maximum(self) -> int:
        while self.maxPrices:
            popped = heapq.heappop(self.maxPrices)
            if (-popped[0]) == self.pricesDict[popped[1]]:
                heapq.heappush(self.maxPrices, popped)
                break
            else:
                heapq.heappush(self.maxPrices, (-self.pricesDict[popped[1]], popped[1]))
        return -self.maxPrices[0][0]
        # return self.pricesDict[self.curMaxTimestamp]

    def minimum(self) -> int:
        while self.minPrices:
            popped = heapq.heappop(self.minPrices)
            if (popped[0]) == self.pricesDict[popped[1]]:
                heapq.heappush(self.minPrices, popped)
                break
            else:
                heapq.heappush(self.minPrices, (self.pricesDict[popped[1]], popped[1]))
        return self.minPrices[0][0]
        # return self.pricesDict[self.curMinTimestamp]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()