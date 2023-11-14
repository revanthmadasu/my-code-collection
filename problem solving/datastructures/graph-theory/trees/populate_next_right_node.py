'''
    Problem: https://leetcode.com/problems/minimum-window-substring/
    concepts: BFS, Trees, Tree Traversal
    performance: 82.99% runtime, 91.45% memory
'''
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        q_l = 1
        while q_l:
            if queue[0] == None:
                break
            # print(q_l)
            # print([node.val for node in queue])
            new_queue = []
            if queue[0].left:
                # print(f'appending 1 {queue[0].left}')
                new_queue.append(queue[0].left)
            if queue[0].right:
                new_queue.append(queue[0].right)
                # print(f'appending 2 {queue[0].right}')
            for i in range(1, len(queue)):
                queue[i-1].next = queue[i]
                if queue[i].left:
                    # print(f'appending 3 {queue[0].left}')
                    new_queue.append(queue[i].left)
                if queue[i].right:
                    # print(f'appending 4 {queue[0].right}')
                    new_queue.append(queue[i].right)
            # queue[-1].next = None
            queue = new_queue
            q_l = len(new_queue)
            if q_l == 0:
                queue.clear()
            # print(f'new q: {queue}, len: {q_l}')
        return root