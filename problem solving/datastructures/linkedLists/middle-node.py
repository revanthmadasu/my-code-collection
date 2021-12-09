'''
URL: https://leetcode.com/problems/middle-of-the-linked-list/
Concepts: Linked Lists
Runtime: 64.74%/100
Memory: 12.03%/100
'''
from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        nodes_map = defaultdict(lambda: None)
        cur_node = head
        while cur_node != None:
            length += 1
            if length % 5 == 0:
                nodes_map[length-1] = cur_node
            cur_node = cur_node.next
        midNode = length // 2
        latestIndex = (midNode//5)*5-1
        if nodes_map[latestIndex] == None:
            latestNode = head
            latestIndex = 0
        else:
            latestNode = nodes_map[latestIndex]
        while latestIndex != midNode:
            latestNode = latestNode.next
            latestIndex += 1
        return latestNode
