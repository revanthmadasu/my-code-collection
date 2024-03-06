'''
    problem: https://leetcode.com/problems/word-break
    concepts: dynamic programming, strings
    performance: 85.70% runtime, 95.99% memory
'''
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictWordOccurrences = dict()
        n = len(s)
        for dictWord in wordDict:
            matched = [(i, i+len(dictWord) - 1) for i in range(n) if s.startswith(dictWord, i)]
            for comb in matched:
                if comb[0] in dictWordOccurrences:
                    dictWordOccurrences[comb[0]].append(comb[1])
                else:
                    dictWordOccurrences[comb[0]] = [comb[1]]
        seqs = [False] * n
        if 0 in dictWordOccurrences:
            for i in dictWordOccurrences[0]:
                seqs[i] = True
        else:
            return False
        for i in range(1,n):
            if i in dictWordOccurrences and seqs[i-1]:
                for end_index in dictWordOccurrences[i]:
                    seqs[end_index] = True
        return seqs[n-1]
            
sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
            