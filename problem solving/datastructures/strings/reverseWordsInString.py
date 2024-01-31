'''
    problem: https://leetcode.com/problems/reverse-words-in-a-string
    concepts: strings
    performance: 76.56% runtime, 86.10% memory
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        words_len = len(words)
        i = words_len - 1
        reversed_order = []
        while i >= 0:
            if len(words[i]):
                reversed_order.append(words[i])
            i -= 1
        return " ".join(reversed_order)