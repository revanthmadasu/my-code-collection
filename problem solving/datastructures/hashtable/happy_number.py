'''
    problem: https://leetcode.com/problems/happy-number
    concepts: hashmap
    performance: 93.48% runtime, 80.05% memory
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        nums_dict = dict()
        while True:
            if n == 1:
                return True
            if n in nums_dict:
                return False
                break
            nums_dict[n] = True
            next_num = 0
            while n != 0:
                next_num += (n%10) ** 2
                n = int(n/10)
            n = next_num