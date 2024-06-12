'''
    Problem: https://leetcode.com/problems/top-k-frequent-elements/
    Concepts: Hash Table, Heap
    performance: 11.11% runtime, 19.64% memory
'''
from typing import List
class Codec:
    def singleEncode(self, string):
        res = ''
        for ch in string:
            if ch == '\\' or ch == '|':
                res += '\\'
            res += ch
        return res
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for string in strs:
            res += (self.singleEncode(string) + '|')
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        curStr = ''
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == '|':
                res.append(curStr)
                curStr = ''
            elif ch == '\\':
                curStr += s[i+1]
                i += 1
            else:
                curStr += ch
            i += 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
'''
fnkd||
fnkd\|\|
fnkd\\\|\\\|
fnjdf|fmkd|ngdjg|fnkd\|\|
'''