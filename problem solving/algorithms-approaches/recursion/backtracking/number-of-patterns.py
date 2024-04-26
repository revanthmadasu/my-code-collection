'''
    Problem: https://leetcode.com/problems/android-unlock-patterns/
    Concepts: Backtracking, DFS, Recursion
    performance: 39.24% runtime, 68.99% memory
'''
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        reqs = dict()
        reqs[1] = {3:2, 9:5, 7:4}
        reqs[2] = {8:5}
        reqs[3] = {1:2, 7:5, 9:6}
        reqs[4] = {6:5}
        reqs[5] = {}
        reqs[6] = {4:5}
        reqs[7] = {1:4, 3:5, 9:8}
        reqs[8] = {2:5}
        reqs[9] = {1:5, 3:6, 7:8}

        def dfs(curPos, visited, size):
            visited = visited.copy()
            visited.append(curPos)
            if len(visited) == size:
                return 1
            res = 0
            for nextPos in range(1, 10):
                if nextPos not in visited and (reqs[curPos][nextPos] in visited if nextPos in reqs[curPos] else True):
                    res += dfs(nextPos, visited, size)
            return res
        patternsCount = 0
        for size in range(m, n+1):
            for start in range(1, 10):
                patternsCount += dfs(start, [], size)
        return patternsCount
