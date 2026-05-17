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

# dfs approach
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def findAll(s, word):
            i = 0
            matchedIndices = []
            while True:
                i = s.find(word, i)
                if i == -1:
                    return matchedIndices
                matchedIndices.append(i)
                i += 1
        wordIntervalsMap = dict()
        for word in wordDict:
            matchedIndices = findAll(s, word)
            # print(f'matched indices for {word}')
            for matchedIndex in matchedIndices:
                # print(f'matched Index: {matchedIndex}')
                if matchedIndex not in wordIntervalsMap:
                    wordIntervalsMap[matchedIndex] = []
                wordIntervalsMap[matchedIndex].append((matchedIndex, matchedIndex + len(word)-1))
        if 0 not in wordIntervalsMap:
            return False
        visited = set()
        q = deque()
        q.extend(wordIntervalsMap[0])
        # print(f'intervals map: {wordIntervalsMap}')
        while len(q):
            # print(f'q is {q}')
            interval = q.pop()
            if interval in visited:
                continue
            if interval[1] == len(s) - 1:
                return True
            visited.add(interval)
            if (interval[1] + 1) in wordIntervalsMap:
                for nextInterval in wordIntervalsMap[interval[1] + 1]:
                    if nextInterval not in visited:
                        q.append(nextInterval)
        return False


sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
            