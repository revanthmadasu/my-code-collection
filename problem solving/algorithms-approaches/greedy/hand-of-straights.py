'''
    problem: https://leetcode.com/problems/hand-of-straights
    concepts: Array, Greedy, Heap, Min Heap, Hashtable
    performance: 75.84% runtime, 30.26% memory
'''
from typing import List
from heapq import heapify, heappop, heappush
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        cardsAvailable = dict()
        for num in hand:
            if num not in cardsAvailable:
                cardsAvailable[num] = 0
            cardsAvailable[num] += 1
        minHeap = list(cardsAvailable.keys())
        heapify(minHeap)
        while len(cardsAvailable):
            notPossible = False
            removed = []
            prev = heappop(minHeap)
            removed.append(prev)
            cardsAvailable[prev] -= 1

            for i in range(1, groupSize):
                if not len(minHeap):
                    return False
                cur = heappop(minHeap)
                cardsAvailable[cur] -= 1
                removed.append(cur)
                if cur == prev + 1:
                    prev = cur
                else:
                    return False
            for cardNum in removed:
                if cardsAvailable[cardNum] > 0:
                    heappush(minHeap, cardNum)
                else:
                    del cardsAvailable[cardNum]
        return True
