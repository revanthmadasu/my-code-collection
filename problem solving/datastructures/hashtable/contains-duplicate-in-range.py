'''
    problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
    concepts: math
    performance: 42.94% runtime, 68.50% memory
'''
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsOcc = dict()
        for i in range(len(nums)):
            if i > k and nums[i-k-1] in numsOcc:
                # print(f'decreasing {i}, numsOcc')
                numsOcc[nums[i-k-1]] -= 1
            if nums[i] in numsOcc and numsOcc[nums[i]]>0:
                # print(i, numsOcc)
                return True
            numsOcc[nums[i]] = (0 if nums[i] not in numsOcc else numsOcc[nums[i]]) + 1
        return False
