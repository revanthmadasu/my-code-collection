'''
    problem: https://leetcode.com/problems/climbing-stairs/
    concepts: dynamic programming, recusion
    performance: 63.36% runtime, 99.52% memory
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1000)
class Solution(object):
    def __init__(self):
        self.result_dict = defaultdict(lambda: None)
        self.result_dict[0] = 0
        self.result_dict[1] = 1
        self.result_dict[2] = 2
        self.result_dict[3] = 3
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.result_dict[n]:
            return self.result_dict[n]
        self.result_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.result_dict[n]
    
        # iterative approach
        # performance: 11.05% runtime, 92.86% memory
        # def climbStairs(self, n):
        #     """
        #     :type n: int
        #     :rtype: int
        #     """
        #     if n <= 3:
        #         return n
        #     n_ways = [0] * n
        #     n_ways[0] = 1
        #     n_ways[1] = 2
        #     for i in range(2, n):
        #         n_ways[i] = n_ways[i-1] + n_ways[i-2]
        #     return n_ways[n-1]

a = Solution()
print(a.climbStairs(2))
print(a.climbStairs(3))
print(a.climbStairs(4))
print(a.result_dict)