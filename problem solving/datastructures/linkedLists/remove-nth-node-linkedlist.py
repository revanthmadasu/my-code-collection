'''
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    Concepts: Linked lists, two pointers
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        trav = head
        l_len = 0
        while trav != None:
            trav = trav.next
            l_len += 1
        node_index = l_len - n
        if node_index == 0:
            return None if l_len <= 1 else head.next
        else:
            trav_i = 0
            trav = head
            prev = head
            while trav != None:
                if trav_i == node_index:
                    prev.next = trav.next
                prev = trav
                trav = trav.next
                trav_i += 1
            return head