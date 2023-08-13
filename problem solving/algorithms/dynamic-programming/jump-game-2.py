'''
    problem: https://leetcode.com/problems/jump-game-ii
    concepts: arrays, dynamic programming
    performance: 30.39% runtime, 48.68% memory
'''
import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        isPossible = [math.inf] * n
        isPossible[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i, min(i + nums[i]+1, n), 1):
                # print(f'i is {i}, j is {j}')
                if isPossible[j] + 1 < isPossible[i]:
                    isPossible[i] = isPossible[j] + 1
                    # print(f'isPossible[{i}] is {isPossible[i]}')
                    # break
        return isPossible[0]