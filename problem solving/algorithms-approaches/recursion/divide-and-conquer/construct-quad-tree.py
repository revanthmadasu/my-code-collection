'''
    problem: https://leetcode.com/problems/construct-quad-tree
    concepts: recursion, divide and conquer
    performance: 32.82% runtime, 15.16% memory
'''
from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recursiveCreate(degree, startI, startJ):
            if len(grid) == 0:
                return None
            if degree == 1:
                return Node(grid[startI][startJ], True, None, None, None, None)
            topLeft = recursiveCreate(degree//2, startI, startJ)
            topRight = recursiveCreate(degree//2, startI, startJ+(degree//2))
            bottomLeft = recursiveCreate(degree//2, startI+(degree//2), startJ)
            bottomRight = recursiveCreate(degree//2, startI+(degree//2), startJ+(degree//2))
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(grid[startI][startJ], True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        res = recursiveCreate(len(grid), 0, 0)
        # print(res)
        return res