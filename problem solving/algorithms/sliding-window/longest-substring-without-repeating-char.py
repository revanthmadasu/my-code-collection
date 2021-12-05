'''
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Concepts: Strings, Sliding Window
Runtime: 164ms => 52.58/100
Memory: 16.5MB => 55.71/100
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_str = ''
        max_str = ''
        startIndex = 0
        cur_chr_map = defaultdict(lambda: None)
        for i in range(len(s)):
            ch = s[i]
            if cur_chr_map[ch] == None:
                cur_str += ch
            else:
                chrs_to_remove = s[startIndex:cur_chr_map[ch]]
                cur_str = s[cur_chr_map[ch]+1:i] + ch
                startIndex = cur_chr_map[ch]+1
                for ch_r in chrs_to_remove:
                    cur_chr_map[ch_r] = None
            cur_chr_map[ch] = i
            if (len(cur_str) > len(max_str)):
                    max_str = cur_str
        return len(max_str)