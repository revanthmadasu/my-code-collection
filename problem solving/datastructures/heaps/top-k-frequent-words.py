'''
    Problem: https://leetcode.com/problems/top-k-frequent-words/
    Concepts: Heap, Max Heap
    performance: 83.28% runtime, 96.80% memory
'''
from typing import List
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maxHeap = []
        wordCount = dict()
        for word in words:
            if word not in wordCount:
                wordCount[word] = 0
            wordCount[word] += 1
        for word in wordCount:
            heapq.heappush(maxHeap, (-wordCount[word], word))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res