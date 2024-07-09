'''
    problem: https://leetcode.com/problems/palindromic-substrings/
    concepts: dynamic programming, Palindrome Dp pattern, String
    performance: 89.45% runtime, 68.64% memory
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalindromesFrom(i):
            palindromes = 0
            for leftright in [(i,i), (i,i+1)]:
                left, right = leftright
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    palindromes += 1
                    left -= 1
                    right += 1
            return palindromes
        palindromeCount = 0
        for i in range(len(s)):
            palindromeCount += getPalindromesFrom(i)
        return palindromeCount