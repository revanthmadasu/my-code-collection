'''
    problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
    concepts: arrays, greedy
    runtime: 99.15% memory: 60.50%
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_price = prices[0]
        profit = 0
        for price in prices:
            if price > cur_price:
                profit += (price-cur_price)
                cur_price = price
            else:
                cur_price = price
        return profit