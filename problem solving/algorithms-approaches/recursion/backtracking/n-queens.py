'''
    problem: https://leetcode.com/problems/n-queens/
    concepts: recursion, backtracking
    performance: 23.93% runtime, 84.75% memory
    #todo: improve runtime
'''
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        sols = []
        res = []
        self.solveRecursively(sols, 0, [])
        # print(sols)
        for sol in sols:
            cur_res = [('.'* q_col) + 'Q' + '.'*(n-q_col-1)for q_col in sol]
            res.append(cur_res)
        return res
    '''
        nth_q: value in range [0, n-1] denoting current row in which queen should be placed
        n_positions: positions of prev queens
    '''
    def solveRecursively(self, sols, nth_q, n_positions):
        # for all positions, check if its being attacked by prev queens
        # print(f'queen: {nth_q}, poss: {n_positions}')
        for i in range(self.n):
            pos_check = (nth_q, i)
            under_attack = False
            for prev_pos_item in enumerate(n_positions):
                if abs(prev_pos_item[0] - pos_check[0]) == abs(prev_pos_item[1] - pos_check[1]) or prev_pos_item[0] == pos_check[0] or prev_pos_item[1] == pos_check[1]:
                    under_attack = True
                    break
            if not under_attack:
                if nth_q == self.n-1:
                    sols.append(n_positions + [i])
                else:
                    self.solveRecursively(sols, nth_q+1, n_positions + [i])
