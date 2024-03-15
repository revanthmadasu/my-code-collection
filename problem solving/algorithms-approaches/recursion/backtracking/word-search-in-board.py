'''
    problem: https://leetcode.com/problems/word-search/
    concepts: recursion, backtracking
    performance: 72.64% runtime, 58.60% memory
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board) # rows
        self.n = len(board[0]) # cols
        self.board = board
        self.word = word
        self.wordLen = len(word)
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == self.word[0][0]:
                    if self.wordLen == 1:
                        return True
                    acc = set()
                    pos = (i,j)
                    acc.add(pos)
                    if self.recursiveSearch(pos, acc, 1):
                        return True
        return False
    def recursiveSearch(self, curPos, accPos, targetLIndex):
        targetLetter = self.word[targetLIndex]
        i, j = curPos
        res = []
        matchedPos = []
        if i+1 < self.m:
            if self.board[i+1][j] == targetLetter:
                matchedPos.append((i+1, j))
        if i-1 >= 0:
            if self.board[i-1][j] == targetLetter:
                matchedPos.append((i-1, j))
        if j+1 < self.n:
            if self.board[i][j+1] == targetLetter:
                matchedPos.append((i, j+1))
        if j-1 >= 0:
            if self.board[i][j-1] == targetLetter:
                matchedPos.append((i, j-1))
        for pos in matchedPos:
            if not (pos in accPos):
                if targetLIndex == self.wordLen - 1:
                    return True
                newAccPos = accPos.copy()
                newAccPos.add(pos)
                res.append(self.recursiveSearch(pos, newAccPos, targetLIndex+1))
        return any(res)
