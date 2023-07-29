'''
    problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    concepts: arrays, two pointers
    runtime: 80.71% memory: 22.66%
'''
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_great_till_i = prices[n-1]
        curr_least_from_i = prices[0]
        great_till_i = []
        least_from_i = []
        for i in range(n):
            great_till_i.append(0)
            least_from_i.append(0)
        for i in range(n):
            if prices[n-1-i] > curr_great_till_i:
                curr_great_till_i = prices[n-1-i]
            if prices[i] < curr_least_from_i:
                curr_least_from_i = prices[i]
            great_till_i[n-1-i] = curr_great_till_i
            least_from_i[i] = curr_least_from_i
        max_profit = -math.inf
        for i in range(n):
            profit = great_till_i[i] - least_from_i[i]
            if profit > max_profit:
                max_profit = profit
        return max(0, max_profit)