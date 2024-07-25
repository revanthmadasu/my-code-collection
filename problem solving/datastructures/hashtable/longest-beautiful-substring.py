'''
    Problem: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
    Concepts: String, Hashtable
    performance: 78.35% runtime, 67.72% memory
'''
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        allowedMap = {
            '':['a'],
            'a':['a','e'],
            'e':['e', 'i'],
            'i':['i','o'],
            'o':['o','u'],
            'u':['u']
        }
        prevChar = ''
        maxLen = 0
        curLen = 0
        for ch in word:
            if ch in allowedMap[prevChar]:
                curLen += 1
                if ch == 'u':
                    maxLen = max(maxLen, curLen)
                prevChar = ch
            else:
                curLen = 0
                prevChar = ''
                if ch == 'a':
                    prevChar = 'a'
                    curLen += 1
        return maxLen