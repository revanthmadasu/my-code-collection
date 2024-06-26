'''
    Problem: https://leetcode.com/problems/subsets-ii/
    Concepts: Backtracking, Recursion, Sets
    performance: 97.01% runtime, 95.86% memory
'''
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = [[]]
        def backTrack(sols, i):
            newSols = []
            for sol in sols:
                newSols.append(sol + [nums[i]])
            sols.extend(newSols)
            if i+1 < len(nums):
                backTrack(sols, i+1)
        backTrack(sols,0)
        uSols = set()
        for sol in sols:
            uSols.add(tuple(sol))
        return list(uSols)