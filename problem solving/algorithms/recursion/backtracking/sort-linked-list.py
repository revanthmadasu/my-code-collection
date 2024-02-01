'''
    problem: https://leetcode.com/problems/sort-list
    concepts: recursion, divide and conquer, linkedlist, sorting, merge-sort
    performance: 5.08% runtime, 39.06% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self.mergeSort(head)
    def getMid(self, node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeSort(self, node):
        print(f'cur node: {node.val}')
        if node.next is None:
            return node
        mid = self.getMid(node)
        right_node = mid.next
        left_node = node
        # splitting in middle
        mid.next = None
        left_sorted = self.mergeSort(left_node)
        right_sorted = self.mergeSort(right_node)
        left_cur = left_sorted
        right_cur = right_sorted
        new_root = new_cur = None
        while left_cur and right_cur:
            if left_cur.val < right_cur.val:
                new_node_val = left_cur.val
                left_cur = left_cur.next
            else:
                new_node_val = right_cur.val
                right_cur = right_cur.next
            new_node = ListNode(new_node_val)
            if not new_root:
                new_root = new_cur = new_node
            else:
                new_cur.next = new_node
                new_cur = new_cur.next
        if left_cur:
            new_cur.next = left_cur
        if right_cur:
            new_cur.next = right_cur
        return new_root
