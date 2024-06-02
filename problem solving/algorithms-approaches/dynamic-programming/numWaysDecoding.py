'''
    problem: https://leetcode.com/problems/decode-ways/
    concepts: Dynamic Programming, String
    performance: 80.52% runtime, 98.76% memory
    #todo: write cleaner code
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return int(s[0] != '0')
        prevRes = 0
        res = 1
        @cache
        def isPairable(i,j):
            if i >= 0 and i < len(s) and j >= 0 and j < len(s):
                ch = s[i]+s[j]
                return ch[0] != '0' and int(ch) <= 26
            return False
        prevRes = 1
        res = 1
        if isPairable(0,1):
            if s[1] != '0':
                res = 2
        else:
            if s[1] == '0':
                return 0
        for i in range(2, len(s)):
            if s[i] == '0':
                if isPairable(i-1, i):
                    if isPairable(i-2, i-1):
                        res = prevRes
                else:
                    return 0
            elif isPairable(i-1, i):
                res, prevRes = res + prevRes, res
            else:
                res, prevRes = res, res
        return res

'''
    123123
    1

    1,2
    12

    1,23
    1,2,3
    12,3

    1,23,1
    1,2,3,1
    12,3,1

    1,23,1,2
    1,2,3,1,2
    12,3,1,2
    1,23,12
    1,2,3,12
    12,3,12
'''