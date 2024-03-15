'''
    problem: https://leetcode.com/problems/valid-palindrome/
    concepts: two pointers, string
    performance: 59.25% runtime, 86.18% memory
'''
class Solution:
    def isPalindrome(self, phrase: str) -> bool:
        s = ""
        for char in phrase:
            if char.isalnum():
                s += char
        s = s.lower()
        i = 0
        n = len(s)
        l = i
        r = n-1-i
        while l <= r:
            if s[l] != s[r]:
                return False
            i += 1
            l = i
            r = n-1-i
        return True