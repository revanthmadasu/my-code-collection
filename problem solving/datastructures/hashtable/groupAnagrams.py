'''
    problem: https://leetcode.com/problems/group-anagrams
    concepts: hashtable
    performance: 96.02% runtime, 95.35% memory
'''
from typing import List
class Solution:
    # time complexity n.k.log(k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = dict()
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString not in strsMap:
                strsMap[sortedString] = [string]
            else:
                strsMap[sortedString].append(string)
        return list(strsMap.values())
    
    # better time complexity n.k, but higher runtime in realtime
    # def getSignature(self, s: str) -> str:
    #     count = [0] * 26
    #     for c in s:
    #         count[ord(c) - ord('a')] += 1
    #     return ''.join([f'{chr(i+ord("a"))}{count[i]}' for i in range(26) if count[i]])

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     strsMap = dict()
    #     for string in strs:
    #         signature = self.getSignature(string)
    #         if signature not in strsMap:
    #             strsMap[signature] = [string]
    #         else:
    #             strsMap[signature].append(string)
    #     return list(strsMap.values())