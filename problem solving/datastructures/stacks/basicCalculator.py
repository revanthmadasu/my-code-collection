'''
    problem: https://leetcode.com/problems/basic-calculator
    concepts: stack
    performance: 6.68% runtime, 85.95% memory
    #todo: reimplement without hard coding. 
'''
class Solution:
    def calculate(self, s: str) -> int:
        self.stack = []
        i = 0
        while i < len(s):
            symbol = s[i]
            #print(f'sym: {i, symbol}')
            increased = False
            if symbol == ' ':
                pass
            elif symbol == ')':
                self.stackReducer()
            elif symbol.isnumeric():
                j = i
                while j < len(s) and s[j].isnumeric():
                    j+= 1
                self.stackPush(s[i:j])
                increased = True
                i = j
            else:
                self.stackPush(symbol)
            if not increased:
                i += 1
        # #print(self.stack)
        return self.stack[0]
    def stackPush(self, symbol):
        stack = self.stack
        #print(f'before push {stack, symbol}')
        # if digit is number, check for top element. 
        try:
            num = int(symbol)
            top = self.getTop() # possible - +, - , (
            if top:
                # if top is +, then there should be an number bottom to it
                if top == '+':
                    operand = self.getBaseOf()
                    operand += num
                    stack.pop()
                    stack.pop()
                    stack.append(operand)
                # bottom element can be a number, ( or nothing
                elif top == '-':
                    if len(stack) > 1:
                        base = self.getBaseOf()
                        if base == '(':
                            stack.pop()
                            stack.append(-num)
                        # base is number case
                        else:
                            stack.pop()
                            stack.pop()
                            stack.append(base-num)
                    else:
                        stack.pop()
                        stack.append(-num)
                # top is (
                elif top == '(':
                    stack.append(num)
                # top is number
                else: 
                    stack.append(int(str(stack.pop())+symbol))
            else:
                stack.append(num)
        except:
            stack.append(symbol)
        #print(f'after push {stack}')
    # called when ) is occured
    def stackReducer(self):
        stack = self.stack
        #print(f'before reduce {stack}')
        acc = 0
        if self.getTop() != '(':
            # base possibilities: -, (
            if self.getBaseOf() == '-':
                num = stack.pop()
                numStr = str(num)
                self.stackPush(numStr)
            else:
                num = stack.pop()
                stack.pop() # (
                numStr = str(num)
                self.stackPush(numStr)
        else:
            stack.pop()
        #print(f'after reduce {stack}')

    def getTop(self):
        return self.stack[len(self.stack)-1] if len(self.stack) else None

    def getBaseOf(self):
        return self.stack[len(self.stack)-2]


