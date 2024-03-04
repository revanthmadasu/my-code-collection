'''
    problem: https://leetcode.com/problems/longest-increasing-subsequence
    concepts: dynamic programming, array
    performance: 8.65% runtime, 67.95% memory
'''
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        i = 0
        while i < n:
            # print(f'cur i: {i}')
            prev_seq_indices = list(filter(lambda l_i: nums[l_i] < nums[i], range(0,i)))
            # print(f'prev seqs: {prev_seq_indices}')
            if len(prev_seq_indices):
                prev_lis_vals = list(map(lambda l_i: lis[l_i], prev_seq_indices))
                # print(f'prev lis vals: {prev_lis_vals}')
                lis[i] += max(prev_lis_vals)
                # print(f'changed lis to : {lis[i]}')

            i += 1
        return max(lis)
        