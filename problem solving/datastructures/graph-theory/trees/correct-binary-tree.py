'''
    problem: https://leetcode.com/problems/correct-a-binary-tree
    concepts: Tree, BFS
    performance: 43.70% runtime, 5.93% memory
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            # print(f'{[node.val for node in q]}')
            newQ = []
            for node in q:
                if node.right and node.right in q:
                    # print('defective node found')
                    if node.dir == 'right':
                        node.parent.right = None
                    else:
                        node.parent.left = None
                    return root
                if node.right:
                    node.right.parent = node
                    node.right.dir = 'right'
                    newQ.append(node.right)
                if node.left:
                    node.left.parent = node
                    node.left.dir = 'left'
                    newQ.append(node.left)
            q = newQ
        return None