'''
    Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree
    Concepts: Tree, BFS, Queue
    performance: 91.72% runtime, 88.37% memory
'''
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            node, dist = q.popleft()
            if not (node.left or node.right):
                return dist
            if node.left:
                q.append((node.left, dist+1))
            if node.right:
                q.append((node.right, dist+1))
        return -1