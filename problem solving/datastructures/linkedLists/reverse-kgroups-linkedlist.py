'''
    problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
    concepts: linked lists
    performance: 100% runtime, 15.16% memory
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#constant space complexity approach
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def hasKNodes(node):
            kCounter = 0
            while node and kCounter < k:
                node = node.next
                kCounter += 1
            return kCounter == k
        def reverseK(node):
            if not hasKNodes(node):
                return node, None, None
            tail = node
            head = None
            curNode = node
            prevNode = None
            nextNode = None
            for i in range(k):
                if not curNode:
                    break
                nextNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                curNode = nextNode
            head = prevNode
            return head, tail, nextNode
        curNode = head
        newRoot = None
        prevNode = None
        while curNode:
            newHead, newTail, nextNode = reverseK(curNode)
            if prevNode:
                prevNode.next = newHead
            if not newRoot:
                newRoot = newHead
            prevNode = newTail
            curNode = nextNode
        return newRoot
            