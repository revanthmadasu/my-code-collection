'''
    problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    concepts: recursion, dfs, binary tree
    performance: 66.36% runtime, 53.22% memory
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getLca(node):
            if not node:
                return None
            if node in [p, q]:
                return node
            l, r = getLca(node.left), getLca(node.right)
            if l and r:
                return node
            return l or r
        return getLca(root)