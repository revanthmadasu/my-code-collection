'''
    problem: https://leetcode.com/problems/length-of-last-word/
    concepts: strings
    performance: 76.32% runtime, 97.58% memory
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = n-1
        l = 0
        while i >= 0:
            if s[i] == ' ':
                if l:
                    return l
                while s[i] == ' ':
                    i -= 1
            l += 1
            i-=1
        return l
        # alternative
        # words = s.split(" ")
        # i = len(words)-1
        # while i >= 0:
        #     l = len(words[i])
        #     if l:
        #         return l
        #     i -= 1
        # return 0
        