'''
    Problem: https://leetcode.com/problems/backspace-string-compare/
    Concepts: String
    performance: 8.96 runtime, 86.89 memory
'''
from typing import List
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def computeBackspaces(string):
            res = ''
            for ch in string:
                if ch == '#':
                    res = res[:-1]
                else:
                    res += ch
            return res
        return computeBackspaces(s) == computeBackspaces(t)