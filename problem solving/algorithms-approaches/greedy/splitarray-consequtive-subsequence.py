'''
    problem: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
    difficulty: medium
    concepts: greedy, hashmaps
    performance: 58.87% runtime, 76.34% memory
'''
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freqMap = dict()
        hypMap = dict()
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        numsKeys = sorted(list(freqMap.keys()))
        def numExists(num):
            return num in freqMap and freqMap[num] > 0
        def checkAndCreateSubsequence(num):
            if numExists(num) and numExists(num+1) and numExists(num+2):
                freqMap[num] = freqMap[num] - 1
                freqMap[num+1] = freqMap[num+1] - 1
                freqMap[num+2] = freqMap[num+2] - 1
                if num+3 not in hypMap:
                    hypMap[num+3] = 0
                hypMap[num+3] += 1
                return True
            return False
        def attachToPrevSeq(num):
            if num in hypMap and hypMap[num] > 0:
                hypMap[num] -= 1
                freqMap[num] -= 1
                if num+1 not in hypMap:
                    hypMap[num+1] = 0
                hypMap[num+1] += 1
                return True
            return False
        for num in numsKeys:
            freq = freqMap[num]
            attachFailed = 0
            for i in range(freq):
                if not attachToPrevSeq(num):
                    attachFailed += 1
            for i in range(attachFailed):
                if not checkAndCreateSubsequence(num):
                    return False
        return True
        