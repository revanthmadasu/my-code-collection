'''
    Problem: https://leetcode.com/problems/add-bold-tag-in-string
    Concepts: Intervals, String
    performance: 73.53 runtime, 41.63 memory
'''
from typing import List
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s
        intervals = []
        for word in words:
            curS = s
            startFrom = 0
            # searchI = curS.find(word)
            while curS.find(word) != -1:
                # print(f'searching {curS} for {word}')
                intervals.append((startFrom+curS.find(word), startFrom+curS.find(word)+len(word)-1))
                startFrom += (curS.find(word)+1)
                curS = curS[curS.find(word)+1:]
                # searchI = curS.find(word)
        
        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(f'all intervals {intervals}')
        merged_intervals = []
        if not intervals:
            return s
        curInterval = intervals[0]
        for interval in intervals:
            if len(merged_intervals):
                curInterval = merged_intervals.pop()
                if curInterval[0] <= interval[0] and interval[0] <= curInterval[1]+1:
                    merged_intervals.append((curInterval[0], max(interval[1], curInterval[1])))
                else:
                    merged_intervals.append(curInterval)
                    merged_intervals.append(interval)
            else:
                merged_intervals.append(interval)
        # for interval in intervals:
        #     if curInterval == None:
        #         curInterval = interval
        #     if curInterval[0] <= interval[0] and interval[0] <= curInterval[1]+1:
        #         curInterval = (curInterval[0], max(interval[1], curInterval[1]))
        #     else:
        #         merged_intervals.append(curInterval)
        #         curInterval = None
        # merged_intervals.append(curInterval)
        res = ""
        cur = 0
        print(merged_intervals)
        for interval in merged_intervals:
            res += s[cur:interval[0]]
            res += (f'<b>{s[interval[0]:interval[1]+1]}</b>')
            cur = interval[1]+1
        res += s[cur:]
        return res