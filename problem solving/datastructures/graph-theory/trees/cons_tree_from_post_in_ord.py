'''
    problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
    concepts: binary tree, tree traversals, divide and conquer, recursion, hash-table
    performance: 50.41% runtime, 5.91% memory
    # todo - improve memory - try if iterative solution improves memory
'''
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = None
        in_index_map = dict()
        print()
        n = len(postorder, )
        for i in range(n):
            in_index_map[inorder[i]] = i
        self.in_index_map = in_index_map
        return self.createTreeRecursively(postorder, inorder)
    def createTreeRecursively(self, postorder, inorder):
        head = postorder[-1]
        head_node = TreeNode(head)
        curr_len = len(postorder)
        # left child is not present
        no_left_child = inorder[0] == head
        no_right_child = inorder[curr_len - 1] == head

        head_in_index = self.in_index_map[head]
        start_in_index = self.in_index_map[inorder[0]]
        cur_head_in_index = head_in_index - start_in_index
        if no_left_child and no_right_child:
            return head_node
        if not no_left_child:
            # print('left exists')
            next_inorder = inorder[0:cur_head_in_index]
            next_postorder = postorder[0:cur_head_in_index]
            head_node.left = self.createTreeRecursively(next_postorder, next_inorder)
        if not no_right_child:
            # print('right exists')
            next_inorder = inorder[cur_head_in_index+1:]
            # todo - to improve runtime use the index map to calculate length
            next_inorder_len = len(next_inorder)
            next_postorder = postorder[-(next_inorder_len+1):-1]
            head_node.right = self.createTreeRecursively(next_postorder, next_inorder)
        return head_node
