'''
    problem: https://leetcode.com/problems/find-median-from-data-stream
    concepts: sorting
    performance: 5% runtime, 98.87% memory
    #todo: improve runtime
'''
class MedianFinder:

    def __init__(self):
        self.nums = [float('-inf'), float('inf')]
        self.medianLeftIndex = -1
        self.medianRightIndex = -1
        self.numsLen = 2

    def addNum(self, num: int) -> None:
        n = len(self.nums)

        for i in range(n):

            if self.nums[i] <= num and num <= self.nums[i+1]:
                self.nums.insert(i+1, num)
                self.numsLen += 1
                return

        self.nums.append(num)
        self.numsLen += 1


    def findMedian(self) -> float:
        if self.numsLen%2 == 0:
            return (self.nums[self.numsLen//2] + self.nums[(self.numsLen//2)-1])/2
        else:
            return self.nums[self.numsLen//2]
