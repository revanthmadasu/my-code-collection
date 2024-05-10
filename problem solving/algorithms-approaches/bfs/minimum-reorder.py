'''
    problem: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
    concepts: BFS, Hashtable
    performance: 8.89% runtime, 5% memory
    #todo: improve performance
'''
from collections import deque
from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        connected = {i : dict() for i in range(n)}
        for conn in connections:
            _from, _to = conn
            if _to not in connected[_from]:
                connected[_from][_to] = dict()
                connected[_from][_to]['out'] = True
            else:
                connected[_from][_to]['out'] = True
            if _from not in connected[_to]:
                connected[_to][_from] = dict()
                connected[_to][_from]['in'] = True
            else:
                connected[_to][_from]['in'] = True
        q = deque()
        q.append(connected[0])
        res = 0
        visited = set()
        visited.add(0)
        # print(f'{connected}')
        while q:
            neighDict = q.popleft()
            for nodeVal in neighDict:
                if nodeVal in visited:
                    continue
                if 'in' not in neighDict[nodeVal]:
                    # print(f'adding for {nodeVal}')
                    res += 1
                q.append(connected[nodeVal])
                visited.add(nodeVal)
        return res