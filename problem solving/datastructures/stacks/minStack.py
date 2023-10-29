'''
    problem: https://leetcode.com/problems/min-stack
    concepts: stacks
    performance: 92.04% runtime, 79.16% memory
'''
import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.cur_min = math.inf
        self.stack_len = 0
        self.min_len = 0

    def push(self, val: int) -> None:
        if val <= self.getMin():
            self.min_stack.append(val)
            self.min_len += 1
        self.stack.append(val)
        self.stack_len += 1

    def pop(self) -> None:
        if self.stack_len:
            self.stack_len -= 1
            val = self.stack.pop()
            if val == self.min_stack[self.min_len - 1]:
                self.min_stack.pop()
                self.min_len -= 1

    def top(self) -> int:
        # print(self.stack)
        if self.stack_len:
            return self.stack[self.stack_len - 1]
        return -1

    def getMin(self) -> int:
        # print(self.min_stack)
        if self.min_len:
            return self.min_stack[self.min_len - 1]
        return math.inf
    
    def parseInput(self,inputCmds, inputs):
        n = len(inputCmds)
        for i in range(1,n):
            out = None
            if inputCmds[i] == "push":
                out = self.push(inputs[i][0])
            elif inputCmds[i] == "pop":
                out = self.pop()
            elif inputCmds[i] == "getMin":
                out = self.getMin()
            elif inputCmds[i] == "top":
                out = self.top() 
            print(out)
def runApp(inpCmds1, inps1):
    ms = MinStack()
    ms.parseInput(inpCmds1, inps1)
    
# inpCmds1 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
# inps1 = [[],[-2],[0],[-3],[],[],[],[]]
# runApp(inpCmds1, inps1)

inpCmds2 = ["MinStack","push","push","push","getMin","pop","getMin"]
inps2 = [[],[0],[1],[0],[],[],[]]
runApp(inpCmds2, inps2)
