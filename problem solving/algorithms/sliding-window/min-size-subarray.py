'''
    problem: https://leetcode.com/problems/minimum-size-subarray-sum
    concepts: sliding window, prefix sum, binary search
    performance: 5% runtime, 33.5% memory
    todo - improve runtime
'''
from typing import List
import math

class Solution:
    def binarySearchIndex(self, cur_index, start, end):
        if end - start <= 1:
            if self.sum_between(cur_index, start) >= self.target:
                return start
            elif self.sum_between(cur_index, end) >= self.target:
                return end
            else:
                return -1
        mid = int((start + end)/2)
        sum_till_mid = self.sum_between(cur_index, mid)
        if sum_till_mid >= self.target:
            return self.binarySearchIndex(cur_index, start, mid)
        else:
            return self.binarySearchIndex(cur_index, mid, end)
        
    def sum_between(self, start, end):
        prev_sum = 0
        if start != 0:
            prev_sum = self.prefix_sum[start-1]
        return self.prefix_sum[end] - prev_sum

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = []
        cur_sum = 0
        self.target = target
        for num in nums:
            cur_sum += num
            if num >= target:
                return 1
            prefix_sum.append(cur_sum)
        n = len(nums)
        if prefix_sum[n-1] < target:
            return 0
        result_size = math.inf
        self.prefix_sum = prefix_sum
        for i in range(n):
            is_possible = self.sum_between(i, n-1) >= target
            if is_possible:
                min_dist_index = self.binarySearchIndex(i, i, n-1)
                if min_dist_index != -1:
                    size = min_dist_index - i + 1
                    if size < result_size:
                        result_size = size
        if result_size == math.inf:
            return 0
        return result_size

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
