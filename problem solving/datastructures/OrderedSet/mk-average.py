'''
    Problem: https://leetcode.com/problems/finding-mk-average/
    Concepts: OrderedSet, Queue, Heap
    performance: 29.40% runtime, 21.79% memory
'''
from collections import deque
from sortedcontainers import SortedList
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
class MKAverage:

    def __init__(self, m: int, k: int):
        self.queue = deque([])
        self.sorted_list = SortedList()
        self.m = m
        self.k = k
        
    def addElement(self, num: int) -> None:
        if len(self.queue) >= self.m: 
            val = self.queue.popleft()
            self.sorted_list.remove(val)
        self.queue.append(num)
        self.sorted_list.add(num)
        
    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m: return -1
        # print(self.sorted_list)
        return sum(
            self.sorted_list[self.k: len(self.sorted_list) - self.k]
        ) // (self.m - self.k * 2)
        
# heap based implementation - time limit exceeds

# import heapq
# import math
# import bisect
# class MKAverage:

#     def __init__(self, m: int, k: int):
#         self.m = m
#         self.k = k
#         self.stream = []
#         #self.leastK = [] # max heap
#         #self.highestK = [] # min heap
#         #heapq.heapify(self.leastK)
#         #heapq.heapify(self.highestK)
#     def addElement(self, num: int) -> None:
#         #heapq.heappush(self.leastK, num)
#         #while len(self.leastK) - len(self.highestK) > 1:
#             #heapq.heappush(self.highestK, -heapq.heappop(self.leastK))
        
#         # bisect.insort(self.stream, num)
#         self.stream.append(num)

#     def calculateMKAverage(self) -> int:
#         if len(self.stream) < self.m:
#             return -1
#         minHeap = self.stream[-self.m:]
#         heapq.heapify(minHeap)
#         for _ in range(self.k):
#             heapq.heappop(minHeap)
#         maxHeap = [-num for num in minHeap]
#         heapq.heapify(maxHeap)
#         for _ in range(self.k):
#             heapq.heappop(maxHeap)
#         remaining = [-num for num in maxHeap]
#         # remaining = self.stream[self.k:-self.k]
#         # print(f'remaining is {remaining}')
#         # print(f'avg if {sum(remaining)/len(maxHeap)}')
#         return math.floor(sum(remaining)/len(remaining))



# # Your MKAverage object will be instantiated and called as such:
# # obj = MKAverage(m, k)
# # obj.addElement(num)
# # param_2 = obj.calculateMKAverage()