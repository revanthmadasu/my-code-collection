'''
    problem: https://leetcode.com/problems/implement-trie-prefix-tree
    concepts: trie
    performance: 78.5% runtime, 70.38% memory
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.childrenMap = {}
        self.isWord = False
    def addChild(self, val):
        if not val in self.childrenMap:
            childNode = Node(val)
            self.childrenMap[val] = childNode
        return self.childrenMap[val]
    def hasChild(self, val):
        return val in self.childrenMap
    def checkAndGetChild(self, val):
        if val in self.childrenMap:
            return self.childrenMap[val]
        return None
class Trie:
        
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            next_node = cur_node.checkAndGetChild(char)
            if next_node == None:
                next_node = cur_node.addChild(char)
            cur_node = next_node
        cur_node.isWord = True


    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            next_node = cur_node.checkAndGetChild(char)
            if next_node == None:
                return False
            cur_node = next_node
        return cur_node.isWord

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            next_node = cur_node.checkAndGetChild(char)
            if next_node == None:
                return False
            cur_node = next_node
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)