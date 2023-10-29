'''
    problem: https://leetcode.com/problems/copy-list-with-random-pointer
    concepts: linked lists
    performance: 48.71% runtime, 11.75% memory
    #todo: improve performance - memory, runtime
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur_node = head
        i = 0
        new_nodes = []
        while cur_node:
            cur_node.index = i
            new_node = Node(cur_node.val)
            new_nodes.append(Node(cur_node.val))
            if i > 0:
                new_nodes[i-1].next = new_nodes[i]
            cur_node = cur_node.next
            i += 1
        n = i
        if not n:
            return None
        cur_node = head
        for i in range(n):
            new_node = new_nodes[i]
            random_node = cur_node.random
            if random_node:
                new_random_node = new_nodes[random_node.index]
                new_node.random = new_random_node
                new_node.random_index = random_node.index
            else:
                new_node.random = None
            cur_node = cur_node.next
        return new_nodes[0]
        