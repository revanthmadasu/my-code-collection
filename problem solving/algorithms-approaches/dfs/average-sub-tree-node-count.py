'''
    Problem: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
    Concepts: DFS, Tree, Binary Tree
    performance: 25.29% runtime, 18.91% memory
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.avgCnt = 0
        # should return sum and count
        def dfs(node):
            leftRes = (0, 0)
            rightRes = (0,0)
            if node.left:
                leftRes = dfs(node.left)
            if node.right:
                rightRes = dfs(node.right)
            count = leftRes[1]+rightRes[1]+1
            _sum = leftRes[0]+rightRes[0]+node.val
            avg = _sum//count
            if avg == node.val:
                self.avgCnt += 1
            return (_sum, count)
        dfs(root)
        return self.avgCnt