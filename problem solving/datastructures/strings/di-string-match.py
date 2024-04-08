'''
    problem: https://leetcode.com/problems/di-string-match/
    concepts: String
    performance: 55.66% runtime, 25.83% memory
'''
from typing import List
from collections import deque
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = [i for i in range(len(s)+1)]
        q = deque(nums)
        res = []
        for ch in s:
            if ch == 'I':
                res.append(q.popleft())
            else:
                res.append(q.pop())
        res.append(q.pop())
        return res