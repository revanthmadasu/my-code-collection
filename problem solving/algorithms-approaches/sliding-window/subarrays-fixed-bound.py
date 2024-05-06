'''
    Problem: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
    Concepts: Sliding Window, Monotonic Queue
    performance: 7.50% runtime, 57.58% memory
'''
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = 0
        r = 0
        outliers = [len(nums)]
        nextMax = [float('inf')]
        nextMin = [float('inf')]
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            outliers.append(i if num < minK or num > maxK else outliers[-1])
            nextMax.append(i if num == maxK else nextMax[-1])
            nextMin.append(i if num == minK else nextMin[-1])
        outliers.reverse()
        nextMin.reverse()
        nextMax.reverse()
        count = 0
        for i in range(len(nums)):
            nextOutlier = outliers[i]
            windowEnd = max(nextMin[i], nextMax[i])
            if windowEnd == float('inf'):
                break
            if nextOutlier > windowEnd:
                count += nextOutlier - windowEnd
        return count

'''
min = 4
max = 8
1,3,4,5,9,8,4,5,8,4,6,4,8,2
8,4,5,8,4,6,4,8,2
0 1 2 3 4 5 6 7 8
8: 7
4: 5
5: 4
8: 4
4: 1
6: 1
4: 1
7,5,4,5,2,2,2
'''