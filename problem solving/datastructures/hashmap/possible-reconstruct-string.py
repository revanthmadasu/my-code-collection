'''
    problem: https://leetcode.com/problems/ransom-note/
    concepts: hashmap/hashtable
    performance: 76.16% runtime, 37.53% memory
'''
from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = defaultdict(lambda: 0)
        for ch in magazine:
            char_count[ch] += 1
        result = True
        for ch in ransomNote:
            if char_count[ch] <= 0:
                result = False
                break
            char_count[ch] -= 1
        return result
