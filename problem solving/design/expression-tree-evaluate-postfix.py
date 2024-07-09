'''
    problem: https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function
    concepts: Stack, Tree
    performance: 89.15% runtime, 17.83% memory
'''
import abc 
from abc import ABC, abstractmethod 
from typing import List
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    def __init__(self, sym, left=None, right=None):
        self.sym = sym
        self.left = left
        self.right = right
        if sym == '+':
            self.symVal = self.left.symVal + self.right.symVal
        elif sym == '-':
            self.symVal = self.left.symVal - self.right.symVal
        elif sym == '*':
            self.symVal = self.left.symVal * self.right.symVal
        elif sym == '/':
            self.symVal = self.left.symVal / self.right.symVal
        else:
            self.symVal = int(sym)
        self.symVal = int(self.symVal)
    # @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        return self.symVal
    


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for sym in postfix:
            newNode = None
            if sym in ['+', '-', '/', '*']:
                right = stack.pop()
                left = stack.pop()
                newNode = Node(sym, left, right)
            else:
                newNode = Node(sym)
            stack.append(newNode)
        return stack[0]
                
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        