'''
    problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
    concepts: stack
    performance: 88.99% runtime, 75.77% memory
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if len(token) > 1 or token.isalnum():
                stack.append(int(token))
            else:
                _l = len(stack)
                op2 = stack.pop(_l-1)
                op1 = stack.pop(_l-2)
                if token == '+':
                    stack.append(op1+op2)
                elif token == '-':
                    stack.append(op1-op2)
                elif token == '*':
                    stack.append(op1*op2)
                elif token == '/':
                    stack.append(int(op1/op2))
        return stack[0]

sol = Solution()

# print(sol.evalRPN(["-2","1","+","3","*"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))