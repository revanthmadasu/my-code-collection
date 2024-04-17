'''
    problem: https://leetcode.com/problems/reorganize-string/
    concepts: Heap, max heap
    performance: 64.62% runtime, 97.32% memory
'''
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCountsMap = dict()
        for ch in s:
            if ch not in charCountsMap:
                charCountsMap[ch] = 0
            charCountsMap[ch] += 1
        maxCount = max(charCountsMap.values())
        if maxCount - (len(s) - maxCount) > 1:
            return ""
        def getMaxHeap():
            heap = [(-charCountsMap[ch], ch)for ch in charCountsMap.keys() if charCountsMap[ch] > 0]
            heapq.heapify(heap)
            return heap
        res = ""
        print('checking in q')
        maxHeap = getMaxHeap()
        while maxHeap:
            hCount, highestCh = maxHeap[0]
            lCount, lowerCh = maxHeap[-1]

            if lowerCh == highestCh:
                if charCountsMap[lowerCh] > 1:
                    # print(f'res created {res}, cur q: {maxHeap}')
                    return ""
                else:
                    return res + lowerCh
            res = res + (highestCh + lowerCh)
            charCountsMap[lowerCh] -= 1
            charCountsMap[highestCh] -= 1
            maxHeap = getMaxHeap()

        return res
