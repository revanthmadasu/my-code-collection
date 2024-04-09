'''
    Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
    Concepts: Loops
    performance: 10.93% runtime, 11.80% memory
    #todo: improve performance - do it in constant time, use math.log
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            if num%2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count