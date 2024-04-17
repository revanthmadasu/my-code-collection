'''
    problem: https://leetcode.com/problems/plates-between-candles/
    concepts: Prefix Sum, LinkedList
    performance: 46.20% runtime, 18.57% memory
'''
from typing import List
class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.next = None
        self.prev = prev
        if prev:
            prev.next = self
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prevCandles = []
        platesPrefixSum = []
        prevCandle = Node(-1)
        for i in range(len(s)):
            prevCount = 0
            if platesPrefixSum:
                prevCount = platesPrefixSum[-1]
            if s[i] == '*':
                prevCount += 1
                platesPrefixSum.append(prevCount)
                prevCandles.append(prevCandle)
            else:
                node = Node(i, prevCandle)
                prevCandle = node
                platesPrefixSum.append(prevCount)
                prevCandles.append(prevCandle)
        ans = []
        for query in queries:
            left, right = query
            leftCandleI, rightCandleI = -1, -1
            if s[left] == '|':
                leftCandleI = left
            else:
                nextNode = prevCandles[left].next
                if nextNode:
                    leftCandleI = nextNode.val
            if s[right] == '|':
                rightCandleI = right
            else:
                # prevNode = prevCandles[right].prev
                # if prevNode:
                rightCandleI = prevCandles[right].val
            # print(f'leftCandleI: {leftCandleI}, rightCandleI: {rightCandleI}')
            if leftCandleI == -1 or rightCandleI == -1:
                ans.append(0)
            else:
                ans.append(max(platesPrefixSum[rightCandleI]-platesPrefixSum[leftCandleI], 0))
        return ans