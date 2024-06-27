'''
    Problem: https://leetcode.com/problems/task-scheduler
    Concepts: Heap, Max Heap, Counting, Queue
    performance: 15.66% runtime, 93.73% memory
'''
from heapq import heappush, heappop
from collections import deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = dict()
        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1
        maxHeap = []
        for key in counts:
            heappush(maxHeap, (-counts[key], key))
        q = deque()
        for i in range(n+1):
            if len(maxHeap):
                count, ch = heappop(maxHeap)
                q.append(ch)
            else:
                q.append("")

        intervalCount = 0
        while len(counts):
            key = q.popleft()
            # else - idle. no need to push to heap do nothing
            if key != "":
                if key in counts:
                    heappush(maxHeap, (-counts[key], key))
            if len(maxHeap):
                insertCount, insertKey = heappop(maxHeap)
                # print(f'insert key- {insertKey} : {insertCount}')
                q.append(insertKey)
                if insertCount == -1:
                    del counts[insertKey]
                else:
                    counts[insertKey] -= 1
            else:
                # idle time. push idle to queue
                q.append("")
            intervalCount += 1
        return intervalCount
