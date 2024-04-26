'''
    Problem: https://leetcode.com/problems/surrounded-regions
    Concepts: matrix, disjointset, union-find
    #incomplete: time limit exceeded for one test case
    #todo: improve performance. check if you can make disjoint set in bulk.
    same problem solved with dfs approach, which has good execution time - check in dfs folder
'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) # m rows
        n = len(board[0]) # n cols
        disjoint_set = DisjointSet()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    disjoint_set.makeSet((i,j), ((i == 0) or (i == m-1) or (j == 0) or (j == n-1)))
                    if i > 0 and board[i-1][j] == 'O':
                        disjoint_set.union((i-1,j), (i,j))
                    if j > 0 and board[i][j-1] == 'O':
                        disjoint_set.union((i,j-1), (i,j))
        all_sets = disjoint_set.getAllSets()
        for _set in all_sets:
            if not _set['isBordered']:
                vals = _set['vals']
                for val in vals:
                    board[val[0]][val[1]] = 'X'

class DisjointSet:
    def __init__(self):
        self.sets_map = {}
    def makeSet(self, val, isBordered):
        new_set = {
            'isBordered': isBordered,
            'vals': {val}
        }
        self.sets_map[val] = new_set
    def find(self, val):
        return self.sets_map[val]
    def union(self, val1, val2):
        # print("in union")
        # print(f'val1 : {val1}')
        # print(f'val2: {val2}')
        set1 = self.sets_map[val1]
        set2 = self.sets_map[val2]
        # print(f'set1: {set1}')
        # print(f'set2: {set2}')

        merged_set = {
            'isBordered': set1['isBordered'] or set2['isBordered'],
            'vals': set1['vals'].union(set2['vals'])
        }

        for val in merged_set['vals']:
            self.sets_map[val] = merged_set
    def getAllSets(self):
        return self.sets_map.values
