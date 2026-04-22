'''
    problem: https://leetcode.com/problems/sort-characters-by-frequency
    concepts: hash table, sorting
    performance: 8.65% runtime, 67.95% memory
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        charCount = dict()
        for ch in s:
            if ch not in charCount:
                charCount[ch] = 1
            else:
                charCount[ch] += 1
        char_counts_list = []
        for key in charCount:
            char_counts_list.append((charCount[key], key))
        char_counts_list.sort(reverse=True)
        res = ""
        for charCountItem in char_counts_list:
            res += charCountItem[1]*charCountItem[0]
        return res