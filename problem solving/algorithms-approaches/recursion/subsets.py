'''
    Problem: https://leetcode.com/problems/subsets
    Concepts: Recursion, Backtracking
    performance: 100% runtime, 78.99% memory
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(pos, curComb, res):
            for i in range(pos+1, len(nums)):
                newComb = curComb + [nums[i]]
                res.append(newComb)
                dfs(i, newComb, res)
        res = [[]]
        dfs(-1, [], res)
        return res

sol = Solution()
print(sol.subsets([1,2,3]))