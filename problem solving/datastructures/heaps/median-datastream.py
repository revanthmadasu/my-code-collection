'''
    problem: https://leetcode.com/problems/find-median-from-data-stream
    concepts: heap
    performance: 47.45% runtime, 31.84% memory
'''
import heapq
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.medianLeftIndex = -1
        self.medianRightIndex = -1
        self.numsLen = 0

        # max heap
        self.lower_heap = []
        heapq.heapify(self.lower_heap)
        # min heap
        self.higher_heap = []
        heapq.heapify(self.higher_heap)

    def addNum(self, num: int) -> None:
        # to get max heap implementation, hack by multiplying with -1
        heapq.heappush(self.lower_heap, -num)
        if len(self.higher_heap):
            while -self.lower_heap[0] > self.higher_heap[0]:
                highest = -heapq.heappop(self.lower_heap)
                lowest = heapq.heappop(self.higher_heap)
                heapq.heappush(self.higher_heap, highest)
                heapq.heappush(self.lower_heap, -lowest)
        while len(self.lower_heap) - len(self.higher_heap) > 1:
            highest = -heapq.heappop(self.lower_heap)
            heapq.heappush(self.higher_heap, highest)



    def findMedian(self) -> float:
        # print(f'first half: {self.lower_heap}, second: {self.higher_heap}')
        if (len(self.lower_heap) + len(self.higher_heap)) % 2 == 0:
            return (-self.lower_heap[0]+self.higher_heap[0])/2
        else:
            return -self.lower_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()