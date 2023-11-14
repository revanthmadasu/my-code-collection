'''
    Problem: https://leetcode.com/problems/binary-tree-right-side-view
    concepts: BFS, tree traversal, trees
    performance: 44.74% runtime, 78.03% memory
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
        res = [root.val]
        q_l = 1
        while q_l:
            if queue[0] == None:
                break
            # print(q_l)
            print([node.val for node in queue])
            new_queue = []
            for i in range(0, len(queue)):
                if queue[i].left:
                    # print(f'appending 3 {queue[0].left}')
                    new_queue.append(queue[i].left)
                if queue[i].right:
                    # print(f'appending 4 {queue[0].right}')
                    new_queue.append(queue[i].right)
            queue = new_queue
            q_l = len(new_queue)
            if q_l == 0:
                queue.clear()
            else:
                res.append(queue[-1].val)
        return res