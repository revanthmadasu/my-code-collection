'''
    problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
    concepts: dynamic programming, multi dimensional DP
    202/214 test cases passed - memory limit exceeded.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        salesMat = [([0]* len(prices)) for i in range(len(prices))]
        # print(f'sales mat: {salesMat}')
        for i in range(len(prices)):
            j = i
            curMax = 0
            while j < len(prices):
                if prices[j] - prices[i] > curMax:
                    curMax = prices[j] - prices[i]
                # print(f'i {i}, j: {j}')
                salesMat[i][j] = curMax
                j += 1
        maxProfit = 0
        maxProfits = []
        for i in range(len(prices)-1, -1, -1):
            if maxProfit < salesMat[i][len(prices)-1]:
                maxProfit = salesMat[i][len(prices)-1]
            maxProfits.append(maxProfit)
        maxProfits.reverse()
        maxProfit = 0
        for i in range(len(prices)-1):
            j = i
            while j < len(prices):
                curProfit = salesMat[i][j]
                if j+1 < len(prices):
                    curProfit += maxProfits[j+1]
                if curProfit > maxProfit:
                    maxProfit = curProfit
                j += 1
        return maxProfit