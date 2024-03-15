'''
    problem: https://leetcode.com/problems/jump-game
    concepts: arrays, dynamic programming
    performance: 16.38% runtime, 66.68% memory
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        isPossible = [False] * n
        isPossible[n-1] = True
        for i in range(n-2, -1, -1):
            for j in range(i, i + nums[i]+1, 1):
                # print(f'i is {i}, j is {j}')
                if isPossible[j]:
                    isPossible[i] = True
                    # print(f'isPossible[{i}] is True')
                    break
        return isPossible[0]