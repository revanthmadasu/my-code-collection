'''
    problem: https://leetcode.com/problems/simplify-path
    concepts: stacks, regex
    performance: 81.98% runtime, 39.40% memory
'''
import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        1) merging of slashes
        2) split by slashes
        3) maintain a stack and perfom pop, push 
        '''
        stack = []
        items = re.split(r'\/+', path)
        n = len(items)
        for i in range(n):
            item = items[i]
            if item == ".":
                continue
            elif item == "..":
                if len(stack) > 1:
                    stack.pop()
            elif item == "":
                if i == 0:
                    stack.append("")
            else:
                stack.append(item)

        if len(stack) == 1:
            return "/"
        else:
            return "/".join(stack)