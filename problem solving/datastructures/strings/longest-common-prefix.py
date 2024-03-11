'''
    problem: https://leetcode.com/problems/longest-common-prefix
    concepts: string
    performance: 80.78% runtime, 91.88% memory
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(len(common)):
            for word in strs:
                if not word[:i+1] == common[:i+1]:
                    return common[:i]
        return common