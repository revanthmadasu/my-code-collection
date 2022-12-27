''''
    https://leetcode.com/problems/add-two-numbers/description/
    Concept: Linked Lists Traversal
    Level: Easy
'''
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = self.getNum(l1)
        sum2 = self.getNum(l2)
        print(sum1+sum2)
        return self.makeList(sum1 + sum2)

    def getNum(self, l):
        multiplier = 1
        trav = l
        num = 0
        while trav != None:
            num += trav.val * multiplier
            multiplier *= 10
            trav = trav.next
        return num

    def makeList(self, num):
        t_num = num
        res_l = ListNode()
        t_l = res_l
        while t_num != 0:
            print("t num is ", t_num)
            t_l.val = t_num % 10
            t_num = math.floor(t_num//10)
            t_l.next = None if t_num == 0 else ListNode()
            t_l = t_l.next
        return res_l