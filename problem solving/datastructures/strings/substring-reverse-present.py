'''
    problem: https://leetcode.com/contest/weekly-contest-389/problems/existence-of-a-substring-in-a-string-and-its-reverse/
    concepts: string
'''
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)-1):
            subStr = s[i:i+2]
            if subStr[::-1] in s:
                # print(subStr[::-1])
                return True
        return False