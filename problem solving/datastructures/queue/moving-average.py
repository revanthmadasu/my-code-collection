'''
    Problem: https://leetcode.com/problems/moving-average-from-data-stream
    Concepts: Queue
    performance: 84.46 runtime, 43.54 memory
'''
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            leftMost = self.window.popleft()
            self.total -= leftMost
        self.window.append(val)
        self.total += val
        return self.total/len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)