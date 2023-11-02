'''
    problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    concepts: linked list, two pointers
    performance: 71.02% runtime, 61.18% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        return self.chainPropogation(None, None, head)
    def chainPropogation(self, acc_head, acc_last, nxt):
        if not nxt:
            return acc_head
        cur_node = nxt
        if cur_node.next and cur_node.next.val == cur_node.val:
            while cur_node and nxt.val == cur_node.val:
                cur_node = cur_node.next
            return self.chainPropogation(acc_head, acc_last, cur_node)
        else:
            if acc_last:
                new_node = ListNode(nxt.val)
                acc_last.next = new_node
                acc_last = new_node
            else:
                acc_head = ListNode(cur_node.val)
                acc_last = acc_head
            return self.chainPropogation(acc_head, acc_last, cur_node.next)
