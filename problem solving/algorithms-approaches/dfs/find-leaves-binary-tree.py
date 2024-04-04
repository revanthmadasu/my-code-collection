'''
    problem: https://leetcode.com/problems/find-leaves-of-binary-tree/
    concepts: DFS, Binary Tree, Tree
    performance: 40.77 runtime, 87.74 memory
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node):
            if not node:
                return -1
            # leaf node
            if (not node.left) and (not node.right):
                if not len(res):
                    res.append([node.val])
                else:
                    res[0].append(node.val)
                return 0
            leftResIndex = -1
            rightResIndex = -1
            if node.left:
                leftResIndex = dfs(node.left)
            if node.right:
                rightResIndex = dfs(node.right)
            insertIndex = max(leftResIndex, rightResIndex)
            if len(res) <= insertIndex+1:
                res.append([node.val])
            else:
                res[insertIndex+1].append(node.val)
            return insertIndex + 1
        # return res
        dfs(root)
        return res
            