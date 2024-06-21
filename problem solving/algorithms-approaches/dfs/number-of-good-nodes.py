'''
    Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
    Concepts: DFS, Trees, Recursion
    performance: 8.37% runtime, 94.55% memory
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
        def dfs(node, path):
            if not node:
                return
            path.append(node.val)
            if node.val >= max(path):
                self.goodCount += 1
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return self.goodCount

            