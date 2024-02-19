'''
    problem: https://leetcode.com/problems/maximum-sum-circular-subarray
    concepts: kadane, array, intervals
    performance: 99.29% runtime, 63.03% memory
    detailed explanation: https://www.youtube.com/watch?v=5WZl3MMT0Eg
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        min_sum = nums[0]
        cur_min_sum = 0
        total = 0
        for num in nums:
            total += num
            if cur_sum + num > 0:
                cur_sum += num
                if cur_sum > max_sum:
                    max_sum = cur_sum
            else:
                cur_sum = 0
                if num > max_sum:
                    max_sum = num
            if cur_min_sum + num < 0:
                cur_min_sum += num
                if cur_min_sum < min_sum:
                    min_sum = cur_min_sum
            else:
                cur_min_sum = 0
                if num < min_sum:
                    min_sum = num
        return (max_sum if max_sum < 0 else max(max_sum, total-min_sum))
        