'''
    problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
    concepts: math
    performance: 99.94% runtime, 52.44% memory
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            # print(haystack[i:i+len(needle)])
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1