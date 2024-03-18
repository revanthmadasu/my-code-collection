'''
    problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
    concepts: dynamic programming, multi dimensional DP
    performance: 98.81% runtime, 98.19% memory
'''
from typing import List
class Solution:
    '''
        Approach: we maitain 2 lists. one for max profit if a stock is sold at current price or before, and one for max profit if a stock is bought at current price or after
        these lists are created using dp approach
        as only 2 transactions are allowed, for a price to get maximum profit, 1st transaction => we add max profit if its sold on or before current price and 2nd transaction => max profit if its bought on or after cur price
    '''
    def maxProfit(self, prices: List[int]) -> int:
        # print('function initialized')
        maxProfitSellAt = []
        maxProfitBuyAt = []
        curMaxProfit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if curMaxProfit < prices[i] - minPrice:
                curMaxProfit = prices[i] - minPrice
            maxProfitSellAt.append(curMaxProfit)
        curMaxProfit = 0
        maxPrice = prices[len(prices)-1]
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
            if curMaxProfit < maxPrice - prices[i]:
                curMaxProfit = maxPrice - prices[i]
            maxProfitBuyAt.append(curMaxProfit)
        maxProfitBuyAt.reverse()
        maxComb = 0
        # print(maxProfitSellAt)
        # print(maxProfitBuyAt)
        for i in range(len(prices)):
            if maxProfitBuyAt[i] + maxProfitSellAt[i] > maxComb:
                maxComb = maxProfitBuyAt[i] + maxProfitSellAt[i]
        return maxComb
# 2d approach - gets correct answer but wrong approach
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         salesMat = [([0]* len(prices)) for i in range(len(prices))]
#         # print(f'sales mat: {salesMat}')
#         for i in range(len(prices)):
#             j = i
#             curMax = 0
#             while j < len(prices):
#                 if prices[j] - prices[i] > curMax:
#                     curMax = prices[j] - prices[i]
#                 # print(f'i {i}, j: {j}')
#                 salesMat[i][j] = curMax
#                 j += 1
#         maxProfit = 0
#         maxProfits = []
#         for i in range(len(prices)-1, -1, -1):
#             if maxProfit < salesMat[i][len(prices)-1]:
#                 maxProfit = salesMat[i][len(prices)-1]
#             maxProfits.append(maxProfit)
#         maxProfits.reverse()
#         maxProfit = 0
#         for i in range(len(prices)-1):
#             j = i
#             while j < len(prices):
#                 curProfit = salesMat[i][j]
#                 if j+1 < len(prices):
#                     curProfit += maxProfits[j+1]
#                 if curProfit > maxProfit:
#                     maxProfit = curProfit
#                 j += 1
#         return maxProfit
    