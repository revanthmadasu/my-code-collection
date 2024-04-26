'''
    Problem: https://leetcode.com/problems/sentence-similarity-ii/
    Concepts: Union Find, String
    performance: 34.72% runtime, 64.93% memory
'''
from typing import List
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similiarityDict = dict()
        wordsDisjointSet = dict()
        uniqueWords = list(set(sentence1).union(set(sentence2)).union(set([pair[0] for pair in similarPairs]).union(set([pair[1] for pair in similarPairs]))))
        for word in uniqueWords:
            wordsDisjointSet[word] = dict()
            wordsDisjointSet[word]['parent'] = word
            wordsDisjointSet[word]['rank'] = 1
        # print(f'unique words: {uniqueWords}, keys: {wordsDisjointSet}')

        def find(word):
            res = word
            while res != wordsDisjointSet[res]['parent']:
                # wordsDisjointSet[res]['parent'] = wordsDisjointSet[res][wordsDisjointSet[res]['parent']]['parent']
                # wordsDisjointSet[res]['parent'] = wordsDisjointSet[wordsDisjointSet[res]['parent']]['parent']
                res = wordsDisjointSet[res]['parent']
            return res
        def union(word1, word2):
            par1, par2 = find(word1), find(word2)
            if par1 == par2:
                return 0
            elif wordsDisjointSet[par1]['rank'] >= wordsDisjointSet[par2]['rank']:
                wordsDisjointSet[par1]['rank'] += wordsDisjointSet[par2]['rank']
                wordsDisjointSet[par2]['parent'] = wordsDisjointSet[par1]['parent']
            else:
                wordsDisjointSet[par2]['rank'] += wordsDisjointSet[par1]['rank']
                wordsDisjointSet[par1]['parent'] = wordsDisjointSet[par2]['parent']
            return 1
        
        for simPair in similarPairs:
            union(simPair[0], simPair[1])
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if not (word1 == word2 or find(word1) == find(word2)):
                return False
        return True