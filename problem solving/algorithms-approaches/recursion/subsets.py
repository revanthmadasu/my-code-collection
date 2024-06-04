'''
    Problem: https://leetcode.com/problems/subsets
    Concepts: Recursion
    performance: 27.09% runtime, 96.93% memory
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursiveSearch(i, sets):
            # print(f'i is {i}')
            _sets2 = []
            for _set in sets:
                _sets2.append(_set+[nums[i]])
            sets.extend(_sets2)
            if i+1 < len(nums):
                recursiveSearch(i+1, sets)
        sets = [[]]
        recursiveSearch(0, sets)
        return sets

sol = Solution()
print(sol.subsets([1,2,3]))