'''
    problem: https://leetcode.com/problems/group-anagrams
    concepts: hashtable
    performance: 96.02% runtime, 95.35% memory
    #todo: check if any better way of implementation exists n*str_len log(str_len) complexity
'''
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = dict()
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString not in strsMap:
                strsMap[sortedString] = [string]
            else:
                strsMap[sortedString].append(string)
        return list(strsMap.values())