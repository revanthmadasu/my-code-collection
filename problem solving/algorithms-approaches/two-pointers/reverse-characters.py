'''
    Problem: https://leetcode.com/problems/reverse-only-letters
    Concepts: Two Pointers, Arrays, String
    performance: 65.17% runtime, 27.27% memory
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start = 0
        end = len(s)-1
        sChars = list(s)
        while start < end:
            while start < end and not s[start].isalpha():
                start += 1
            while end > start and not s[end].isalpha():
                end -= 1
            sChars[start], sChars[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(sChars)