'''
    problem: https://leetcode.com/problems/knight-probability-in-chessboard/
    concepts: Dynamic Programming, Recursion
    performance: 26.84 runtime, 7.34 memory
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def dp(pos, k):
            if k < 0:
                return 1
            if pos[0] >= n or pos[0] < 0 or pos[1] >= n or pos[1] < 0:
                return 0
            if (pos, k) in visited:
                return visited[(pos, k)]
            moves = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
            prob = 0
            for move in moves:
                prob += (dp((pos[0]+move[0], pos[1]+move[1]), k-1) / 8)
            visited[(pos, k)] = prob
            return prob
        visited = dict()
        return dp((row, column), k)
