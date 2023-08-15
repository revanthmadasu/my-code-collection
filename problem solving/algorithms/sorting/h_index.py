'''
    problem: https://leetcode.com/problems/h-index
    concepts: arrays, sorting
    performance: 70.57% runtime, 84.50% memory
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        result = 0
        for i, citation in enumerate(citations):
            result = max(result, min(citation, n-i))
        return result