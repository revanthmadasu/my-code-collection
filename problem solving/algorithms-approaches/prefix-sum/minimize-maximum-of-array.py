'''
    Problem: https://leetcode.com/problems/minimize-maximum-of-array/
    Concepts: Prefix Sum, Dynamic Programming
    Performance: 20.31% runtime, 36.66% memory
'''
from typing import List
import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum = []
        _sum = 0
        for num in nums:
            _sum += num
            prefixSum.append(_sum)
        for i in range(len(nums)-1, 0, -1):
            # print(f'{nums}')
            prevAvg = prefixSum[i-1]/(i)
            if nums[i] > prevAvg:
                curAvg = (prevAvg*i + nums[i])/(i+1)
                diff = math.ceil(nums[i]-curAvg)
                nums[i] -= diff
                nums[i-1] += diff
                prefixSum[i-1] += diff
            
        return max(nums)
        # brute force approach
        # def getMaxNumIndex():
        #     maxNumIndex = 0
        #     for i in range(len(nums)):
        #         if nums[i] > nums[maxNumIndex]:
        #             maxNumIndex = i
        #     return maxNumIndex
        # while True:
        #     # print(f'nums: {nums}')
        #     maxNumIndex = getMaxNumIndex()
        #     if maxNumIndex > 0 and nums[maxNumIndex] > 0 and nums[maxNumIndex] - nums[maxNumIndex-1] > 0:
        #         change = math.ceil((nums[maxNumIndex] - nums[maxNumIndex-1])/2)
        #         nums[maxNumIndex] -= change
        #         nums[maxNumIndex-1] += change
        #     else:
        #         break
        # return max(nums)