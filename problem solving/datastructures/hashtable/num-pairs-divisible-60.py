'''
    Problem: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    Concepts: HashTable, Combinatorics
    Performance: 90.03% runtime, 93.82% memory
'''
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timesDict = dict()
        for i in range(len(time)):
            time[i] = time[i]%60
            if time[i] not in timesDict:
                timesDict[time[i]] = 0
            timesDict[time[i]] += 1
        res = 0
        visited = set()
        # print(timesDict)
        for timeKey in timesDict:
            if timeKey in visited:
                continue
            reqTime = (60 - timeKey) % 60
            if timeKey == reqTime:
                res += int(timesDict[timeKey] * (timesDict[timeKey]-1) * 0.5)
                visited.add(timeKey)
            elif reqTime in timesDict:
                res += (timesDict[timeKey] * timesDict[reqTime])
                visited.add(timeKey)
                visited.add(reqTime)
        return res

        # brute force
        # for i in range(len(time)-1):
        #     for j in range(i+1, len(time)):
        #         if (time[i]+time[j])%60 == 0:
        #             res.add((i, j))
        # return len(res)