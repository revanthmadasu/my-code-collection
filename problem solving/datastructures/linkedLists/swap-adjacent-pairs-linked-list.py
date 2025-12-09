'''
    Problem: https://leetcode.com/problems/swap-nodes-in-pairs
    Concepts: Linked list
    performance: 100% runtime, 82.56% memory
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        firstNode = head
        secondNode = head.next
        newHead = secondNode
        if not secondNode:
            return firstNode
        prevNode = None
        

        while firstNode and secondNode:
            nextFirstNode = secondNode.next
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            if prevNode:
                prevNode.next = secondNode
            prevNode = firstNode
            firstNode = nextFirstNode
            if firstNode:
                secondNode = firstNode.next
        return newHead