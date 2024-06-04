'''
    Problem: https://leetcode.com/problems/longest-palindrome
    Concepts: String, Hashtable
    performance: 70.41% runtime, 34.50% memory
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        lettersCount = dict()
        for ch in s:
            if ch not in lettersCount:
                lettersCount[ch] = 0
            lettersCount[ch] += 1
        counts = sorted(lettersCount.values())
        counts = counts[::-1]
        maxLen = 0
        containsOdd = False
        for count in counts:
            if count%2 == 1:
                containsOdd = True
            maxLen += (count if count%2 == 0 else (count - 1))
        if containsOdd:
            maxLen += 1
        return maxLen