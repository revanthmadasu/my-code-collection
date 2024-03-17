'''
    problem: https://leetcode.com/contest/weekly-contest-389/problems/count-substrings-starting-and-ending-with-given-character/
    concepts: string
'''
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        substringCount = 0
        for ch in s:
            if ch == c:
                substringCount += 1
        res = 0
        for i in range(1, substringCount+1):
            res += i
        return res
                