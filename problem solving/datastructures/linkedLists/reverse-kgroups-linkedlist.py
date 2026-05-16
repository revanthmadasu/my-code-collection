'''
    problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
    concepts: linked lists, recursion
    performance: 100% runtime, 15.16% memory
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def hasKNodes(node):
            kCounter = 0
            while node and kCounter < k:
                node = node.next
                kCounter += 1
            return kCounter == k
        def recursivelyReverseK(node):
            if not hasKNodes(node):
                return node
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
            if nextNode:
                tail.next = nextNode
                nextKHead = recursivelyReverseK(nextNode)
                tail.next = nextKHead
            return head
        
        return recursivelyReverseK(head)
            