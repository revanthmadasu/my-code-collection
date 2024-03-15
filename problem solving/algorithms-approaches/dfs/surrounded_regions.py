'''
    Problem: https://leetcode.com/problems/surrounded-regions
    Concepts: matrix, dfs, recursion
    performance: 87.2% runtime, 23.41% memory
'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) # m rows
        n = len(board[0]) # n cols
        bordered = []
        for i in range(m):
            bordered.append([False] * n)
        def dfs(i, j):
            # print(f'dfs: i: {i}, j: {j}')
            nonlocal board, bordered, m, n
            bordered[i][j] = True
            if (i-1 >= 0) and (not bordered[i-1][j]) and (board[i-1][j] == 'O'):
                dfs(i-1, j)
            if (i+1 < m) and (not bordered[i+1][j])  and (board[i+1][j] == 'O'):
                dfs(i+1, j)
            if (j-1 >= 0) and (not bordered[i][j-1]) and (board[i][j-1] == 'O'):
                dfs(i, j-1)
            if (j+1 < n) and (not bordered[i][j+1]) and (board[i][j+1] == 'O'):
                dfs(i, j+1)
        for j in range(n):
            if (not bordered[0][j]) and board[0][j] == 'O':
                dfs(0, j)
            if (not bordered[m-1][j]) and board[m-1][j] == 'O':
                dfs(m-1, j)
        for i in range(m):
            if (not bordered[i][0]) and board[i][0] == 'O':
                dfs(i, 0)
            if (not bordered[i][n-1]) and board[i][n-1] == 'O':
                dfs(i, n-1)
        print(bordered)
        for i in range(m):
            for j in range(n):
                if not bordered[i][j]:
                    board[i][j] = 'X'
