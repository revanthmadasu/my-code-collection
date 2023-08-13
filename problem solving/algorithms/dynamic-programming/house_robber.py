'''
    problem: https://leetcode.com/problems/house-robber
    concepts: dynamic programming, arrays, memoization
    performance: 86.32% runtime, 39.63% memory
'''
import math
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        v_max = [-math.inf] * n
        if n == 1:
            return nums[0]
        for i in range(n-1, -1, -1):
            first_choice = -math.inf
            second_choice = -math.inf
            first_choice_i = i + 2
            second_choice_i = i + 3
            if first_choice_i < n:
                first_choice = v_max[first_choice_i]
            if second_choice_i < n:
                second_choice = v_max[second_choice_i]
            # print(f'for nums[{i}]= {nums[i]} firstChoice: {first_choice}, secondChoice: {second_choice}')
            v_max[i] = nums[i] + max(first_choice, second_choice, 0)
        print(v_max)
        return max(v_max[0], v_max[1])