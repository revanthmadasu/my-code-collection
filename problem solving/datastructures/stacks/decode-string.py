'''
    problem: https://leetcode.com/problems/greatest-common-divisor-of-strings
    concepts: stack
    performance: 53.43% runtime, 51.05% memory
'''
class Solution:
    def decodeString(self, s: str) -> str:
        curPos = 0
        stack = []
        while curPos < len(s):
            symb = s[curPos]
            if symb.isnumeric():
                num = ""
                # print(f'{curPos}')
                while curPos < len(s) and s[curPos].isnumeric():
                    num += s[curPos]
                    curPos += 1
                stack.append(int(num))
            elif symb == '[':
                stack.append(symb)
                curPos += 1
            elif symb.isalpha():
                word = ""
                while curPos < len(s) and s[curPos].isalpha():
                    word += s[curPos]
                    curPos += 1
                if len(stack) and stack[len(stack)-1].isalpha():
                    top = stack.pop()
                    stack.append(top+word)
                else:
                    stack.append(word)
            elif symb == ']':
                
                word = stack.pop()
                # print(f'word is {num}')

                br = stack.pop() # [
                # print(f'br is {br}')

                num = stack.pop()
                # print(f'num is {num}')
                decoded = num*word
                if len(stack) and stack[len(stack)-1].isalpha():
                    top = stack.pop()
                    stack.append(top+decoded)
                else:
                    stack.append(decoded)
                curPos += 1
            # print(f'stack is {stack}')
        return stack[len(stack)-1]
