'''
    problem: https://leetcode.com/problems/word-search/
    concepts: recursion, backtracking
    performance: 72.64% runtime, 58.60% memory
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(curPos, path):
            wordSearchIndex = len(path)
            if len(path) == len(word):
                return True
            nextPositions = [pos for pos in [(curPos[0]+1, curPos[1]), (curPos[0]-1, curPos[1]), (curPos[0], curPos[1]+1), (curPos[0], curPos[1]-1)] if pos[0] < m and pos[0] >= 0 and pos[1] < n and pos[1] >= 0 and pos not in path and board[pos[0]][pos[1]] == word[wordSearchIndex]]
            if wordSearchIndex == len(word) - 1 and len(nextPositions) > 0:
                return True
            for pos in nextPositions:
                if dfs(pos, path+[pos]):
                    return True
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    pos = (i,j)
                    if dfs(pos, [pos]):
                        return True
        return False