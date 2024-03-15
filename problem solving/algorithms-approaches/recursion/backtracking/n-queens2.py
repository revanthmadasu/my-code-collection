'''
    problem: https://leetcode.com/problems/n-queens/
    concepts: recursion, backtracking
    performance: 15.88% runtime, 86.46% memory
    #todo: improve runtime
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.numSols = 0
        self.solveRecursively(0, [])
        return self.numSols
    '''
        nth_q: value in range [0, n-1] denoting current row in which queen should be placed
        n_positions: positions of prev queens
    '''
    def solveRecursively(self, nth_q, n_positions):
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
                    self.numSols += 1
                else:
                    self.solveRecursively(nth_q+1, n_positions + [i])