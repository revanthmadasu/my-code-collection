'''
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Concepts: Strings, Sliding Window, Hashtable
Runtime: 164ms => 52.58/100
Memory: 16.5MB => 55.71/100
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countsDict = dict()
        left = 0
        right = 0
        curSubstringLength = 0
        maxSubstringLength = 0
        while left <= right and right < len(s):
            while s[right] in countsDict and countsDict[s[right]] > 0:
                curSubstringLength -= 1
                countsDict[s[left]] = countsDict[s[left]] - 1
                left += 1
            countsDict[s[right]] = 1
            right += 1
            curSubstringLength += 1
            maxSubstringLength = max(maxSubstringLength, curSubstringLength)
        return maxSubstringLength