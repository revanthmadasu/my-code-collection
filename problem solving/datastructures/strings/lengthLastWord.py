'''
    problem: https://leetcode.com/problems/length-of-last-word/
    concepts: strings
    performance: 36.50% runtime, 92.38% memory
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        i = len(words)-1
        while i >= 0:
            l = len(words[i])
            if l:
                return l
            i -= 1
        return 0
        