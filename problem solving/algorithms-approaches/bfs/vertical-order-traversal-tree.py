'''
    Problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree
    Concepts: BFS, Binary Tree, Tree, Queue, Sorting
    performance: 98.62% runtime, 70.59% memory
'''
from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque() # item - (node, row, col)
        colNodes = dict()
        q.append((root, 0, 0))
        while q:
            qItem = q.popleft()
            if qItem[2] not in colNodes:
                colNodes[qItem[2]] = []
            node = qItem[0]
            colNodes[qItem[2]].append((qItem[1], node.val))
            if node.left:
                q.append((node.left, qItem[1]+1, qItem[2]-1))
            if node.right:
                q.append((node.right, qItem[1]+1, qItem[2]+1))
        keys = [key for key in colNodes]
        keys.sort()
        res = []
        for key in keys:
            res.append([item[1] for item in sorted(colNodes[key])])
        return res
