'''
    problem: https://leetcode.com/problems/minimum-number-of-keypresses
    concepts: Heap, max heap
    performance: 18.29% runtime, 95.34% memory
    #todo - improve runtime - try with sorting instead of heaps
'''
import heapq
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        posCounts = [0,0,0]
        curPos = 0
        charCounts = dict()
        for ch in s:
            if ch not in charCounts:
                charCounts[ch] = 0
            charCounts[ch] += 1
        maxHeap = [(-charCounts[ch], ch) for ch in charCounts.keys()]
        heapq.heapify(maxHeap)
        buttonsCount = 0
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            if posCounts[curPos] == 9:
                curPos += 1
            # print(f'typing {ch} for {-count}*{curPos+1}={-(curPos+1)*(count)} times')
            buttonsCount += ((-count) * (curPos+1))
            posCounts[curPos] += 1
        return buttonsCount