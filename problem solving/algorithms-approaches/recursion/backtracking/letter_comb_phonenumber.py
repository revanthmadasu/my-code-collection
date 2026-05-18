'''
    problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number
    concepts: recursion, backtracking
    performance: 100% runtime, 40% memory
'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numAlphMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backtrack(curDigits):
            if len(curDigits) == 1:
                return numAlphMap[curDigits[0]]
            preRes = backtrack(curDigits[1:])
            curRes = []
            for sub in preRes:
                for ch in numAlphMap[curDigits[0]]:
                    curRes.append(ch+sub)
            return curRes
        return backtrack(digits)