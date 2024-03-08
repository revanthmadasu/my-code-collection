'''
    problem: https://leetcode.com/problems/find-median-from-data-stream
    concepts: sorting
    performance: 10.96% runtime, 94.42% memory
    #todo: improve runtime
'''
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.medianLeftIndex = -1
        self.medianRightIndex = -1
        self.numsLen = 0

    def addNum(self, num: int) -> None:
        # n = len(self.nums)
        if self.numsLen == 0:
            self.nums.append(num)
            self.numsLen += 1
            return
        # recursive search - runtime: 10%
        i = self.recursiveSearch(num, 0, self.numsLen-1)
        self.nums.insert(i, num)
        self.numsLen += 1
        #     # linear search ============== runtime: 5%
        # for i in range(n):
        #     if self.nums[i] <= num and num <= self.nums[i+1]:
        #         self.nums.insert(i+1, num)
        #         self.numsLen += 1
        #         return
        # self.nums.append(num)
        # self.numsLen += 1
        # ================


    def recursiveSearch(self, num, start, end):
        # print(f'searching for {num} in range [{start}, {end}]')
        # only 1 number in array
        if end-start <= 1:
            if num < self.nums[start] or num == self.nums[start]:
                return start
            elif num == self.nums[end] or num > self.nums[end]:
                return end+1
            elif num > self.nums[start] and num < self.nums[end]:
                return end
            else:
                print('error')
                return -1
        mid = (start+end)//2
        if num < self.nums[mid]:
            return self.recursiveSearch(num, start, mid)
        elif num > self.nums[mid]:
            return self.recursiveSearch(num, mid, end)
        else:
            return mid


    def findMedian(self) -> float:
        if self.numsLen%2 == 0:
            return (self.nums[self.numsLen//2] + self.nums[(self.numsLen//2)-1])/2
        else:
            return self.nums[self.numsLen//2]
