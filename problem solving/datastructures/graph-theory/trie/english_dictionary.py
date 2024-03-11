'''
    problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/
    concepts: trie
    performance: 34.66% runtime, 72.06% memory
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
            return [self.childrenMap[val]]
        elif val == '.':
            return list(self.childrenMap.values())
        return []
class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            next_nodes = cur_node.checkAndGetChild(char)
            if len(next_nodes) == 0:
                next_node = cur_node.addChild(char)
            else:
                next_node = next_nodes[0]
            cur_node = next_node
        cur_node.isWord = True


    def search(self, word: str) -> bool:
        cur_node = self.root
        queue = [cur_node]
        found = False
        n = len(word)
        for i in range(n):
            char = word[i]
            new_queue = []
            char_found = False
            for cur_node in queue:
                next_nodes = cur_node.checkAndGetChild(char)
                if len(next_nodes) == 0:
                    char_found = char_found or False
                else: 
                    char_found = True
                    new_queue.extend(next_nodes)
            queue = new_queue
            if i == n-1:
                for node in queue:
                    found = found or node.isWord
            else:
                if len(queue) == 0:
                    found = False
                    break
        return found


# Your WordDictionary object will be instantiated and called as such:
# input 1 =================>
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))
# print(obj.search("bad"))
# print(obj.search(".ad"))
# print(obj.search("b.."))
# ===========================

# input 2 =================>
# obj2 = WordDictionary()
# print(obj2.search("a"))
# ===========================

# input 3 =================>
obj3 = WordDictionary()
obj3.addWord("at")
obj3.addWord("and")
obj3.addWord("an")
obj3.addWord("add")
print(obj3.search("a"))
print(obj3.search(".at"))
obj3.addWord("bat")
print(obj3.search(".at"))
print(obj3.search("an."))
print(obj3.search("a.d."))
print(obj3.search("b."))
print(obj3.search("a.d"))
print(obj3.search("."))
# ===========================
# param_2 = obj.search(word)