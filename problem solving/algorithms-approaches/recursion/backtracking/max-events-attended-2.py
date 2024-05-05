'''
    problem: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
    concepts: Dynamic Programming, Recursion, Backtracking, Intervals, Sorting
    performance: 26.67% runtime, 79.52% memory
'''
class Solution:
    def recursiveSelect(self, events, pos, k):
        if k <= 0 or pos >= len(events):
            return 0
        if self.cache[k-1][pos] != None:
            return self.cache[k-1][pos]
        nextPos = self.getNextEvent(events, pos)
        select = events[pos][2] + self.recursiveSelect(events, nextPos, k-1)
        reject = self.recursiveSelect(events, pos+1, k)
        self.cache[k-1][pos] = max(select, reject)
        return self.cache[k-1][pos]
    def getNextEvent(self, events, pos):
        selectedEvent = events[pos]
        start = pos+1
        end = len(events)
        while start < end:
            mid = (start + end) // 2
            if events[mid][0] > selectedEvent[1]:
                end = mid
            else:
                start = mid + 1
        return end
    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.cache = [[None for i in range(len(events))] for j in range(k)]
        events.sort(key = lambda event: (event[0], event[1]))
        return self.recursiveSelect(events, 0, k)