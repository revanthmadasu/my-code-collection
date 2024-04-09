'''
    Problem: https://leetcode.com/problems/brace-expansion/
    Concepts: BFS
    performance: 69.10% runtime, 75.54% memory
'''
from typing import List
class Solution:
    def expand(self, s: str) -> List[str]:
        q = ['']
        i = 0
        while i < len(s):
            newQ = []
            if s[i].isalpha():
                for q_i in q:
                    newQ.append(q_i + s[i])
                i += 1
            else:
                nextCloseI = s.index('}', i)
                chars = s[i+1:nextCloseI].split(',')
                for q_i in q:
                    for char in chars:
                        newQ.append(q_i + char)
                i = nextCloseI + 1
            q = newQ
        q.sort()
        return q