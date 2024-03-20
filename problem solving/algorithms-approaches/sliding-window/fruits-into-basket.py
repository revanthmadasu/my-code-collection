'''
    problem: https://leetcode.com/problems/fruit-into-baskets
    concepts: sliding window
    performance: 93.86% runtime, 53.11% memory
'''
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seqCount = 0
        c = fruits[0]
        p = None
        count = 0
        maxCount = 0
        for i, fruit in enumerate(fruits):
            if p is None or fruit in [c, p]:
                if fruit == c:
                    seqCount += 1
                    if i-1 >= 0:
                        count += 1
                    else:
                        count = 1
                else:
                    p, c = c, fruit
                    seqCount = 1
                    count += 1
            else:
                count = seqCount + 1
                seqCount = 1
                p, c = c, fruit
            maxCount = max(count, maxCount)
        return maxCount

