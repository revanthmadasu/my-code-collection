'''
    problem: https://leetcode.com/problems/battleships-in-a-board/
    concepts: DFS, Recursion
    performance: 14.68% runtime, 14.55% memory
    #todo: improve performance
'''
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        shipsCount = 0
        def dfs(pos):
            visited.add(pos)
            i,j = pos
            if i+1 < len(board) and board[i+1][j] == 'X':
                dfs((i+1, j))
            elif j+1 < len(board[0]) and board[i][j+1] == 'X':
                dfs((i, j+1))
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i,j) not in visited:
                    shipsCount += 1
                    dfs((i,j))
        return shipsCount