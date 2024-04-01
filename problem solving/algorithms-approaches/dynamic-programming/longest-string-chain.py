'''
    Problem: https://leetcode.com/problems/longest-string-chain/
    Concepts: Dynamic Programming
    performance: 27.15% runtime, 43.93% memory
'''
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda word: len(word))
        print(words)
        dp = []
        prevSizeIndex = -1
        curSize = 0
        def isPredecessor(predecWord, word):
            if len(word)-len(predecWord) != 1:
                return False
            for i in range(len(word)):
                # print(f'comparing {predecWord} with {word[:i] + word[i+1:]}')
                if predecWord == (word[:i] + word[i+1:]):
                    return True
            return False

        for i in range(len(words)):
            if len(words[i]) > curSize:
                prevSizeIndex = i-1
                curSize = len(words[i]) 
            j = prevSizeIndex
            maxChain = 1
            while j >= 0 and len(words[j]) == curSize -1:
                if isPredecessor(words[j], words[i]):
                    maxChain = max(dp[j]+1, maxChain)
                j -= 1
            dp.append(maxChain)
        print(dp)
        return max(dp)