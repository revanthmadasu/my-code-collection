#!/bin/python3

# https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        return ''
    def peek(self):
        if len(self.stack):        
            return self.stack[len(self.stack) - 1]
        return ''
    def length(self):
        return len(self.stack)
    
def isBalanced(s):
    stack = Stack()
    bracketOpen = {
        '(': True,
        '[': True,
        '{': True,
        ')': False,
        ']': False,
        '}': False
    }
    bracketPair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '': ''
    }
    unbalanced = False
    for bracket in s:
        if bracketOpen[bracket]:
            stack.push(bracket)
        elif bracketPair[stack.peek()] == bracket:
                stack.pop()
        else:
            unbalanced = True
            break
    if (stack.length() == 0) and not unbalanced:
        return 'YES'
    else:
        return 'NO' 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
