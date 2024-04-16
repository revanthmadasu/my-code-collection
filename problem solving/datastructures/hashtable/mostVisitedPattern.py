'''
    problem: https://leetcode.com/problems/analyze-user-website-visit-pattern/
    concepts: HashTable, Sorting
    performance: 57.38% runtime, 41.22% memory
'''
from typing import List
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        indices = sorted(list(range(n)), key=lambda i: timestamp[i])
        # print(indices)
        userFlows = dict()
        for i in indices:
            if username[i] not in userFlows:
                userFlows[username[i]] = []
            userFlows[username[i]].append(website[i])
        userPatterns = dict()
        # print(userFlows)
        for user in userFlows.keys():
            window = userFlows[user]
            seen = set()
            for i in range(len(window)):
                for j in range(i+1, len(window)):
                    for k in range(j+1, len(window)):
                        pattern = (window[i], window[j], window[k])
                        if pattern in seen:
                            continue
                        seen.add(pattern)
                        if pattern not in userPatterns:
                            userPatterns[pattern] = 0
                        userPatterns[pattern] += 1
        maxPatternLen = max(userPatterns.values())
        # print(userPatterns)
        # print(maxPatternLen)
        minPattern = None
        for pattern in userPatterns.keys():
            if userPatterns[pattern] == maxPatternLen:
                print(pattern)
                if not minPattern:
                    minPattern = pattern
                else:
                    minPattern = min(pattern, minPattern)
        return minPattern
