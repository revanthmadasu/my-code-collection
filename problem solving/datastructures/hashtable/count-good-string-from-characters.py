'''
    problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
    concepts: Hashtable, String
    performance: 15.43% runtime, 40.30% memory
'''
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def getCountDict(string):
            charCount = dict()
            for ch in string:
                if ch not in charCount:
                    charCount[ch] = 0
                charCount[ch] += 1
            return charCount
        charCount = getCountDict(chars)
        res = 0
        for word in words:
            wordCharCount = getCountDict(word)
            possible = True
            for ch in wordCharCount:
                if ch not in charCount or charCount[ch] < wordCharCount[ch]:
                    possible = False
                    break
            if possible:
                res += len(word)
        return res