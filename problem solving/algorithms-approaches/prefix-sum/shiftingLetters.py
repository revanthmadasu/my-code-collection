'''
    Problem: https://leetcode.com/problems/shifting-letters/
    Concepts: Prefix Sum, String, Asci
    performance: 64.65% runtime, 31.68% memory
'''
from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        prefixSum = []
        _sum = 0
        for shift in shifts:
            prefixSum.append(_sum + shift)
            _sum += shift
        prefixSum.reverse()
        res = ''
        # print(f'{prefixSum}')
        for i in range(len(s)):
            ch = s[i]
            shiftedCh = chr(ord('a')+(prefixSum[i]+(ord(ch)-ord('a')))%26)
            res += shiftedCh
        return res