'''
    problem: https://leetcode.com/problems/isomorphic-strings
    concepts: hashmap/hashtable, asci codes, strings
    performance: 73.66% runtime, 97.44% memory
'''
class Solution(object):
    def getNumStr(self, s):
        cur_uniq_char_id = ord('A')
        char_exists = {}
        res = ''
        for ch in s:
            if not char_exists.has_key(ch):
                char_exists[ch] = cur_uniq_char_id
                cur_uniq_char_id += 1
            res += chr(char_exists[ch])
        return res
            

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.getNumStr(s) == self.getNumStr(t)
        