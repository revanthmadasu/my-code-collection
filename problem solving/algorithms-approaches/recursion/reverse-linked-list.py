'''
    Problem: https://leetcode.com/problems/reverse-linked-list/
    Concepts: Linked List, Recursion
    performance: 90.07% Runtime 72.31% Memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if not node:
                return None, None
            if not node.next:
                return node, node
            head, tail = dfs(node.next)
            tail.next = node
            node.next = None
            return head, node
        rev_head, tail = dfs(head)
        return rev_head
# class Solution:
#     def reverseList(self, head, root=True):
#         if not head:
#             return head
#         new_node = ListNode(head.val)
#         if head.next:
#             next_node = self.reverseList(head.next, False)
#             next_node.next = new_node
#             if root:
#                 return self.reversed
#             return new_node
#         else: 
#             self.reversed = new_node
#             return new_node
