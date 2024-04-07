'''
    problem: https://leetcode.com/problems/detonate-the-maximum-bombs
    concepts: DFS
    performance: 18.98 runtime, 5.03 memory
'''

from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        propogations = [set([i]) for i in range(n)]
        for i in range(n):
            for j in range(n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
                if dist <= r1:
                    propogations[i].add(j)

        def dfs(curIndex):
            if curIndex in visited:
                return
            visited.add(curIndex)
            for nextBomb in propogations[curIndex]:
                dfs(nextBomb)
        res = 0
        for i in range(n):
            visited = set()
            dfs(i)
            res = max(res, len(visited))

        return res