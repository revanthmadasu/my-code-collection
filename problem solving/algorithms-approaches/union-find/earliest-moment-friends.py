'''
    Problem: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
    Concepts: Union Find
    performance: 37.62% runtime, 99.24% memory
'''
from typing import List
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda log: log[0])
        parents = [i for i in range(n)]
        ranks = [1] * n
        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return 0
            if ranks[px] > ranks[py]:
                parents[px] = parents[py]
                ranks[py] += ranks[px]
            else:
                parents[py] = parents[px]
                ranks[px] += ranks[py]
            return 1
        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        for log in logs:
            # print(f'adding {log}')
            union(log[1], log[2])
            # print(f'parents: {parents}, ranks: {ranks}')
            if ranks[find(log[1])] == n:
                return log[0]
        # print('not possible')
        print(parents)
        return -1