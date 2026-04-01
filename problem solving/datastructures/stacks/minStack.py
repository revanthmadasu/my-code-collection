'''
    problem: https://leetcode.com/problems/min-stack
    concepts: stacks
    performance: 92.04% runtime, 79.16% memory
'''
class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        data = (val, len(self.stack))
        if not (len(self.minStack) and self.minStack[len(self.minStack)-1][0] < val):
            self.minStack.append(data)
        self.stack.append(data)
        # print(f'after push({val}), stack: {self.stack}, minStack: {self.minStack}')

    def pop(self) -> None:
        data = self.stack.pop()
        if data == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()
        # print(f'after pop->({data}), stack: {self.stack}, minStack: {self.minStack}')
        return data[0]

    def top(self) -> int:
        return self.stack[len(self.stack)-1][0]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1][0]
    
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
