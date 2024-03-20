'''
    problem: https://leetcode.com/problems/factorial-trailing-zeroes
    concepts: math logic
    performance: 16.91% runtime, 46.90% memory
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def getCounts(num):
            twoCount = 0
            fiveCount = 0
            while num%2 == 0 and num > 1:
                twoCount += 1
                num = num / 2
            while num%5 == 0 and num > 1:
                fiveCount += 1
                num /= 5
            return (twoCount, fiveCount)
        twoCount = 0
        fiveCount = 0
        while n > 0:
            c_t, c_f = getCounts(n)
            twoCount += c_t
            fiveCount += c_f
            n -= 1
        return min(twoCount, fiveCount)