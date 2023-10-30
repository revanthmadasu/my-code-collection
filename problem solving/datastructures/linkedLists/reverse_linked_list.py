'''
    problem: https://leetcode.com/problems/reverse-linked-list-ii/
    concepts: linked lists
    performance: 91.27% runtime, 82.32% memory
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        reverse_interval = []
        leftNode = None
        rightNode = None
        cur_node = head
        i = 1
        while i != left:
            cur_node = cur_node.next
            i += 1
        leftNode = cur_node
        while i != right:
            reverse_interval.append(cur_node.val)
            cur_node = cur_node.next
            i += 1
        rightNode = cur_node
        reverse_interval.append(cur_node.val)
        cur_node = leftNode

        i = 0
        print(reverse_interval)
        while cur_node:
            print(i)
            cur_node.val = reverse_interval[right - left - i]
            if cur_node == rightNode:
                break
            cur_node = cur_node.next
            i += 1

        return head
