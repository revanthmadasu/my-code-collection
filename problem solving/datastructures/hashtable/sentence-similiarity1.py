'''
    Problem: https://leetcode.com/problems/sentence-similarity
    Concepts: Hashtable, String
    performance: 14.15% runtime, 82.93% memory
'''
from typing import List
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similiarityDict = dict()
        for simPair in similarPairs:
            if simPair[0] not in similiarityDict:
                similiarityDict[simPair[0]] = set()
            if simPair[1] not in similiarityDict:
                similiarityDict[simPair[1]] = set()
            similiarityDict[simPair[1]].add(simPair[0])
            similiarityDict[simPair[0]].add(simPair[1])
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if not (word1 == word2 or (word1 in similiarityDict and word2 in similiarityDict[word1])):
                return False
        return True