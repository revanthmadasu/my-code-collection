'''
    problem: https://leetcode.com/problems/game-of-life
    concepts: matrices
    performance: 98.7% runtime, 94.2% memory
'''
import copy
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        m rows, n columns
        """
        m = len(board)
        n = len(board[0])
        board_or = copy.deepcopy(board)
        def get_neighbours(fixed_i, same_row = False):
            live_neighbour_count = 0
            live_neighbour_count += (
                int(j-1 >= 0 and board_or[fixed_i][j-1] == 1) + 
                int(board_or[fixed_i][j] == 1 and not same_row) + 
                int(j+1 < n and board_or[fixed_i][j+1] == 1)
                )

            return live_neighbour_count
        for i in range(m):
            for j in range(n):
                live_neighbour_count = 0
                if i-1 >= 0:
                    live_neighbour_count += get_neighbours(i-1)
                if i+1 < m:
                    live_neighbour_count += get_neighbours(i+1)

                live_neighbour_count += get_neighbours(i, True)
                if board[i][j] == 1:
                    if live_neighbour_count < 2 or live_neighbour_count > 3:
                        board[i][j] = 0
                else:
                    if live_neighbour_count == 3:
                        board[i][j] = 1
        return board
sol = Solution()
board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board2 = [[0,0]]
print(sol.gameOfLife(board2))