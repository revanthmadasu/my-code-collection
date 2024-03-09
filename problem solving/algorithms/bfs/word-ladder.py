'''
    problem: https://leetcode.com/problems/word-ladder/
    concepts: BFS, Hashtable
    performance: 11.92% runtime, 98.27% memory
    #todo - improve runtime
'''
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = dict()
        queue = [beginWord]
        visited[beginWord] = True
        def isDiffOne(str1, str2):
            if len(str1) != len(str2):
                return False
            n = len(str1)
            matched = False
            for i in range(n):
                if str1[i] != str2[i]:
                    if matched == True:
                        return False
                    matched = True
            return matched
        chainCount = 1
        while len(queue) != 0:
            # print(f'queue : {queue}')
            chainCount += 1
            newQueue = []
            for queueItem in queue:
                for word in wordList:
                    if (not (word in visited)) and isDiffOne(queueItem, word):
                        if word == endWord:
                            return chainCount
                        newQueue.append(word)
                        visited[word] = True
            queue = newQueue
        return 0