'''
    problem: https://leetcode.com/contest/weekly-contest-390/problems/maximum-length-substring-with-two-occurrences/
    concepts: string
'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        lettersCount = dict()
        start = 0
        maxLen = 0
        for i, letter in enumerate(s):
            if letter not in lettersCount:
                lettersCount[letter] = 0
            lettersCount[letter] += 1
            while lettersCount[s[i]] > 2:
                lettersCount[s[start]] -= 1
                start += 1
            # if i - start+1 >maxLen:
            #     print(s[start:i+1])
            maxLen = max(i - start+1, maxLen)
        return maxLen