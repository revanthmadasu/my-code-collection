'''
    Problem: https://leetcode.com/problems/palindrome-partitioning
    Concepts: Backtracking, Recursion, Dynamic Programming, Caching
    performance: 95.92% runtime, 79.93% memory
'''
from functools import cache
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def getSubstringPartitions(s):
            # print(f'received: {s}')
            if len(s) == 1:
                return [[s]]
            elif len(s) == 0:
                return [[]]
            res = []
            for j in range(len(s)):
                substr = s[0:j+1]
                if substr == substr[::-1]:
                    partitions = getSubstringPartitions(s[j+1:])
                    for partition in partitions:
                        res.append([substr] + partition)
            return res
        return getSubstringPartitions(s)