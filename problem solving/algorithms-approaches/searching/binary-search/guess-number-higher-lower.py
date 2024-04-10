'''
    Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
    Concepts: Searching, Binary Search
    performance: 22.90% runtime, 15.10% memory
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = (start+end) // 2
            compRes = guess(mid)
            if compRes == -1:
                end = mid-1
            elif compRes == 0:
                return mid
            else:
                start = mid+1
        return start
        