'''
    problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list
    concepts: Linked list
    performance: 8.17% runtime, 7.34% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getLen(node):
            if node is None:
                return 0
            return getLen(node.next) + 1
        def getNode(node, num, curNum=0):
            # print(f'at {curNum}')
            curNum += 1
            if num == curNum:
                return node
            return getNode(node.next, num, curNum)
        n = getLen(head)
        end = n+1-k
        start = k
        start, end = min(start, end), max(start, end)
        if start == end:
            return head
        # print(f'searching for {start}')
        startNode = getNode(head, start)
        # print(f'found {start} - {startNode.val}')
        
        # print(f'searching for {end}')
        endNode = getNode(head, end)
        # print(f'found {end} - {endNode.val}')
        
        # print(f'searching for {end-1}')
        endPrev = getNode(head, end-1)
        # print(f'found {end-1} - {endPrev.val}')

        nextEnd = endNode.next
        if start+1 != end:
            endNode.next = startNode.next
            endPrev.next = startNode
        else:
            endNode.next = startNode
        startNode.next = nextEnd
        if start > 1:
            # print(f'searching for {start-1}')
            startPrev = getNode(head, start-1)
            # print(f'found {start} - {startPrev.val}')
            startPrev.next = endNode
        return head if start != 1 else endNode
            
        