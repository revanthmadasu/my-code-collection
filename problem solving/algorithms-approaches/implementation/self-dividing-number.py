'''
    Problem: https://leetcode.com/problems/self-dividing-numbers/
    Concepts: Loops
    performance: 80.20% runtime, 68.66% memory
'''
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            curNum = num
            while curNum:
                digit = curNum % 10
                
                if digit == 0 or num % digit != 0:
                    return False
                curNum = curNum // 10
            return True
        return [num for num in range(left, right+1) if isSelfDividing(num)]