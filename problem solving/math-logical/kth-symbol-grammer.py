'''
    problem: https://leetcode.com/problems/k-th-symbol-in-grammar
    concepts: Math
    performance: 85.93 runtime, 54.14 memory
'''
'''
0
01
0110
01101001
k = 15 -> 7 -> 3 -> 1

14 -> 6 -> 2 -> 0
8 -> 4 -> 2 -> 1
0110100110010110
k k   k       k
'''
import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curK = k
        revertCount = 0
        while curK > 1:
            # print(f'k is {curK}')
            lastIndex = 2 ** math.ceil(math.log(curK, 2))
            diff = lastIndex - curK
            # print(f'diff is {diff}')
            curK = lastIndex//2 - diff
            # print(f'k changed to {curK}')
            revertCount += 1
        return revertCount%2
