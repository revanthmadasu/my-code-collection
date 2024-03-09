'''
    problem: https://leetcode.com/problems/sqrtx
    concepts: math
    performance: 88.82% runtime, 53.01% memory
'''
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))