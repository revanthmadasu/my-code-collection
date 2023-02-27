'''
    https://leetcode.com/problems/reverse-linked-list/
    Concepts: Linked List, Recursion
    47.5% Runtime 6.42% Memory
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head, root=True):
        if not head:
            return head
        new_node = ListNode(head.val)
        if head.next:
            next_node = self.reverseList(head.next, False)
            next_node.next = new_node
            if root:
                return self.reversed
            return new_node
        else: 
            self.reversed = new_node
            return new_node