'''
    Problem: https://leetcode.com/problems/time-needed-to-buy-tickets/
    Concepts: Arrays
    performance: 90.06% runtime, 51.50% memory
'''
from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        waitTime = 0
        for i in range(len(tickets)):
            if i <= k:
                waitTime += min(tickets[i], tickets[k])
            else:
                waitTime += min(tickets[i]-1 if tickets[i] >= tickets[k] else tickets[i], tickets[k]-1)
        return waitTime
    # brute force - performance: 46.57% runtime, 5.07% memory
    # def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    #     waitTime = 0
    #     while True:
    #         for i in range(len(tickets)):
    #             if tickets[i] != 0:
    #                 waitTime += 1
    #                 tickets[i] -= 1
    #                 if tickets[i] == 0 and i == k:
    #                     return waitTime
    #     return -1 