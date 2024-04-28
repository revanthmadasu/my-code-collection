'''
    Problem: https://leetcode.com/problems/alien-dictionary/
    Concepts: Topological Sorting, Graph, DFS, Post order dfs
    performance: 32.57% runtime, 6.09% memory
    #todo: revise - https://www.youtube.com/watch?v=Q9PIxaNGnig
'''
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        ordersDetermined = []
        maxWord = ""
        for i in range(len(words)):
            word = words[i]
            maxWord = word if len(word) > len(maxWord) else maxWord
            if i+1 < len(words):
                word1, word2 = words[i], words[i+1]
                minLen = min(len(word1), len(word2))
                if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                    return ""
        checkingWords = words
        for i in range(0, len(maxWord)):
            j = 0
            remove = set()
            while j < len(checkingWords):
                k = j
                starting = checkingWords[j][:i]
                while k < len(checkingWords) and checkingWords[k][:i] == starting:
                    k += 1
                order = []
                prev = ''
                for word in checkingWords[j:k]:
                    if prev != word[i]:
                        order.append(word[i])
                        prev = word[i]
                if len(order) > 1:
                    ordersDetermined.append(order)
                # else:
                #     ordersUndetermined.append(checkingWords[j][i:])
                #     remove.add(checkingWords[j])
                j = k
            checkingWords = [word for word in checkingWords if len(word) > i+1 and word not in remove]
        print(ordersDetermined)
        for order in ordersDetermined:
            for i in range(len(order)):
                for j in range(i+1, len(order)):
                    adj[order[i]].add(order[j])
        print(adj)
        visited = dict()
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nextC in adj[c]:
                if dfs(nextC):
                    return ""
            visited[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return ''.join(res)

        # print(ordersUndetermined)
        # return ""