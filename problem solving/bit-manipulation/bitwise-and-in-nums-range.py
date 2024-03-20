'''
    problem: https://leetcode.com/problems/bitwise-and-of-numbers-range
    concepts: bit manipulation
    #incomplete: 3 testcases failing
    #todo - complete it
'''
import math
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        if left == 0 or right == 0:
            return 0
        if math.floor(math.log(left, 2)) != math.floor(math.log(right, 2)):
            return 0

        for num in range(left+1, right+1):
            res = res & num
            if res == 0:
                break
        return res