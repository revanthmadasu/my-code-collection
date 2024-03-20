'''
    problem: https://leetcode.com/problems/bitwise-and-of-numbers-range
    concepts: bit manipulation
    performance: 85.95% runtime, 66.34% memory
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right &=(right-1)
        return right
        # res = left
        # if left == 0 or right == 0:
        #     return 0
        # if math.floor(math.log(left, 2)) != math.floor(math.log(right, 2)):
        #     return 0

        # for num in range(left+1, right+1):
        #     res = res & num
        #     if res == 0:
        #         break
        # return res