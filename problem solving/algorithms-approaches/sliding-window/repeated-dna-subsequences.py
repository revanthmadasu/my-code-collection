'''
    problem: https://leetcode.com/problems/repeated-dna-sequences/
    concepts: Sliding Window, Hashtable
    performance: 57.43% runtime, 83.67% memory
'''
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subStrCount = dict()
        for i in range(len(s)-9):
            subStr = s[i:i+10]
            if subStr not in subStrCount:
                subStrCount[subStr] = 0
            subStrCount[subStr] += 1
        return [key for key in subStrCount.keys() if subStrCount[key] > 1]