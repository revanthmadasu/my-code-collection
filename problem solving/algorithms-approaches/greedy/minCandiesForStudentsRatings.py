'''
    problem: https://leetcode.com/problems/candy/
    concepts: arrays, greedy, array traversal
    performance: 71.4% runtime, 52.9% memory
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i-1]+1, candies[i])
        res = candies[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i]  > ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])
            res += candies[i]
        return res