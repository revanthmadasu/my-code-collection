'''
    Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
    Concepts: DFS, Trees, Recursion
    performance: 53.82% runtime, 39.09% memory
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0
        def dfs(node):
            prevMax = self.curMax
            if not node:
                return
            self.curMax = max(self.curMax, node.val)
            if node.val >= self.curMax:
                self.goodCount += 1
            dfs(node.left)
            dfs(node.right)
            self.curMax = prevMax
        self.curMax = root.val
        dfs(root)
        return self.goodCount  