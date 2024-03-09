'''
    problem: https://leetcode.com/problems/plus-one/
    concepts: math
    performance: 24.82% runtime, 87.01% memory
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] % 10 != 0:
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits