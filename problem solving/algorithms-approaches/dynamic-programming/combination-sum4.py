'''
    Problem: https://leetcode.com/problems/combination-sum-iv/
    Concepts: Backtracking, Dynamic Programming, Recursion
    performance: 85.35% runtime, 14.08% memory
'''
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(target, res = 0):
            for num in nums:
                if num < target:
                    res += dfs(target-num)
                elif num == target:
                    res += 1
            return res
        return dfs(target)