#!/bin/python3
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import math
import os
import random
import re
import sys
from collections import defaultdict
def ncr(n,r):
    print(f'num is {n}')
    numerator = math.factorial(n)
    denomerator = math.factorial(n-r) * math.factorial(r)
    return int(numerator/denomerator)
def countTriplets(arr, r):
    elementCountMap = defaultdict(lambda: None)
    total = 0
    for num in arr:
        elementCountMap[num] = (elementCountMap[num] or 0) + 1
    for num in elementCountMap.keys():
        if (num * r) in elementCountMap and (num * r * r) in elementCountMap:    
            count1 = elementCountMap[num]
            count2 = elementCountMap[num * r]
            count3 = elementCountMap[num * r * r]
            if count2 and count3:
                if (num == (num * r) == (num * r * r)):
                    if (count1 >= 3):
                        total += ncr(count1,3)
                else:
                    total += (count1 * count2 * count3)
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
