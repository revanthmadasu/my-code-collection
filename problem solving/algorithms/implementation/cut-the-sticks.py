#!/bin/python3

#https://www.hackerrank.com/challenges/cut-the-sticks/problem

import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    currArr = arr[:]
    result = []
    while True:
        n = len(currArr)  
        if n == 0:
            break      
        minimum = min(currArr)
        average = sum(currArr)/n
        result.append(n)
        i = 0
        while i<len(currArr):
            if currArr[i] == minimum:
                currArr.pop(i)
            elif currArr[i] > minimum:
                currArr[i] = currArr[i] - minimum
                i = i+1
            else:
                i = i+1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
