'''
    Problem: https://leetcode.com/problems/binary-tree-right-side-view
    concepts: BFS, tree traversal, trees
    performance: 100.00% runtime, 80.95% memory
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while len(queue):
            newQueue = []
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            res.append(queue[-1].val)
            queue = newQueue
        return res