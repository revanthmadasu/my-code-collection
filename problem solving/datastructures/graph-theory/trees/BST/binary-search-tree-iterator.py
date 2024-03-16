'''
    problem: https://leetcode.com/problems/binary-search-tree-iterator
    concepts: tree traversal, resursion
    performance: 49.93% runtime, 70.19% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def inOrderTraversal(self, node):
        res = []
        if node.left:
            res.extend(self.inOrderTraversal(node.left))
        res.append(node.val)
        if node.right:
            res.extend(self.inOrderTraversal(node.right))
        return res

    def __init__(self, root: Optional[TreeNode]):
        self.nums = self.inOrderTraversal(root)
        self.cur = -1


    def next(self) -> int:
        self.cur += 1
        return self.nums[self.cur]

    def hasNext(self) -> bool:
        return self.cur+1 < len(self.nums)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()