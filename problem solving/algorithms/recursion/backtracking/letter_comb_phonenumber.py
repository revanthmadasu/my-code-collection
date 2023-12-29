'''
    problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number
    concepts: recursion, backtracking
    performance: 30.29% runtime, 9.43% memory
    #todo: improve memory
'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.numAlphMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        return self.backtrack(digits)
    def backtrack(self, digits):
        len_digits = len(digits)
        if len_digits == 1:
            return self.numAlphMap[digits[0]]
        elif len_digits == 0:
            return []
        else:
            next_combs = self.backtrack(digits[1:])
            new_combs = []
            for comb in next_combs:
                for char in self.numAlphMap[digits[0]]:
                    new_combs.append(char+comb)
            return new_combs