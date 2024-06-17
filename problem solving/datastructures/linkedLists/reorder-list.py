'''
    Problem: https://leetcode.com/problems/reorder-list/
    Concepts: Linked List
    performance: 5.36% runtime, 94.97% memory
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curNode = head
        while curNode:
            nodes.append(curNode)
            curNode = curNode.next
        if len(nodes) == 1:
            return
        prevNode = None
        for i in range(len(nodes)//2):
            nodes[i].next = nodes[-(i+1)]
            if prevNode:
                prevNode.next = nodes[i]
            prevNode = nodes[-(i+1)]
        if len(nodes)%2 == 1:
            prevNode.next = nodes[len(nodes)//2]
            nodes[len(nodes)//2].next = None
        else:
            prevNode.next = None
        