'''
URL: https://leetcode.com/problems/permutation-in-string
Concepts: Strings, Sliding Window, Hashtable
Runtime: 164ms => 52.58/100
Memory: 16.5MB => 55.71/100
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1CountsMap = dict()
        for ch in s1:
            if ch not in s1CountsMap:
                s1CountsMap[ch] = 1
            else:
                s1CountsMap[ch] = s1CountsMap[ch] + 1
        left = 0
        right = 0
        s2MatchedCountsMap = dict()
        def isMatched():
            for ch in s1CountsMap:
                if ch not in s2MatchedCountsMap or s2MatchedCountsMap[ch] < s1CountsMap[ch]:
                    return False
            return True
        while right < len(s2):
            # print('hello')
            while right < len(s2) and ((s2[right] not in s1CountsMap) or (s2[right] in s2MatchedCountsMap and s2MatchedCountsMap[s2[right]] >= s1CountsMap[s2[right]])):
                if s2[left] in s2MatchedCountsMap:
                    s2MatchedCountsMap[s2[left]] = max(s2MatchedCountsMap[s2[left]] - 1, 0)
                left += 1
                right = max(left, right)
                # print(f'right: {right}')
            if right >= len(s2):
                return False
            if s2[right] not in s2MatchedCountsMap:
                s2MatchedCountsMap[s2[right]] = 1
            else:
                s2MatchedCountsMap[s2[right]] = s2MatchedCountsMap[s2[right]] + 1
            right += 1
            # print(f'cur string: {s2[left:right]}')
            if isMatched():
                return True
        return False
                