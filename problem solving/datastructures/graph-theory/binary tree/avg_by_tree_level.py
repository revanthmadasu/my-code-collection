'''
    Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/
    concepts: BFS, tree traversal, trees
    performance: 5.36% runtime, 78.80% memory
    # todo - improve runtime
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = [root]
        res = [root.val]
        q_l = 1
        while q_l:
            if queue[0] == None:
                break
            # print(q_l)
            # print([node.val for node in queue])
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
                res.append(mean([node.val for node in queue]))
        return res