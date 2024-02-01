'''
    problem: https://leetcode.com/problems/valid-anagram
    concepts: string
    performance: 83.13% runtime, 65.83% memory
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersCount = dict()
        for ch in s:
            lettersCount[ch] = (lettersCount[ch] if ch in lettersCount else 0) + 1
        for ch in t:
            if ch in lettersCount:
                if not lettersCount[ch]:
                    return False
                lettersCount[ch] -= 1
            else:
                return False
        for ch in s:
            if lettersCount[ch]:
                return False
        return True