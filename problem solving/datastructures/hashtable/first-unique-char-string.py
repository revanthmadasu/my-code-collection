'''
    Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
    Concepts: Hashtable, String
    performance: 9.82% Runtime 35.65% Memory
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCounts = dict()
        for i in range(len(s)):
            if s[i] not in charCounts:
                charCounts[s[i]] = 0
            charCounts[s[i]] += 1
        for i in range(len(s)):
            if charCounts[s[i]] == 1:
                return i
        return -1