'''
    problem: https://leetcode.com/problems/word-search-ii/
    concepts: trie, recursion, backtracking, dfs
    performance: 30.57% runtime, 61.29% memory
    explanation: https://www.youtube.com/watch?v=asbcE9mZz_U
'''
from typing import List
class TrieNode:
    def __init__(self, val):
        self.childNodesMap =dict()
        self.val = val
        self.isWord = False

    def addChild(self, val):
        if val in self.childNodesMap:
            return self.childNodesMap[val]
        childNode = TrieNode(val)
        self.childNodesMap[val] = childNode
        return childNode

    def addWord(self, word):
        curNode = self
        for i in range(len(word)):
            if word[i] in curNode.childNodesMap:
                curNode = curNode.childNodesMap[word[i]]
            else:
                curNode = curNode.addChild(word[i])
        curNode.isWord = True

    def getChildWith(self, val):
        if val in self.childNodesMap:
            return self.childNodesMap[val]
        else:
            return None
    def searchString(self, searchString):
        curNode = self
        for i in range(len(searchString)):
            if curNode.getChildWith(searchString[i]):
                curNode = curNode.getChildWith(searchString[i])
            else:
                return False
        return True

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        m = len(board)
        n = len(board[0])
        self.m = m
        self.n = n
        root = TrieNode('')
        for word in words:
            root.addWord(word)
        res, visited = set(), set()        
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >=m or c >= n or (r,c) in visited or board[r][c] not in node.childNodesMap:
                return
            visited.add((r,c))
            word += board[r][c]
            node = node.childNodesMap[board[r][c]]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
        for i in range(m):
            for j in range(n):
                # print(f'currently creating for ({i},{j})')
                dfs(i, j, root, '')
        return list(res)
        # return [word for word in words if root.searchString(word)]

  
    
sol = Solution()
board = [
    ['A', 'N', 'D', 'B'],
    ['B', 'T', 'I', 'S'],
    ['A', 'I', 'T', 'T'],
    ['S', 'T', 'N', 'D']
]
words = ['AND', 'BAND', 'TIT', 'ABTIT']
board2 = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words2 = ["oath","pea","eat","rain"]
print(sol.findWords(board, words))
print(sol.findWords(board2, words2))
