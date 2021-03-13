#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import statistics
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
def isValid(s):
    lettersCountMap = defaultdict(lambda: None)
    for letter in s:
        lettersCountMap[letter] = ((lettersCountMap[letter] or 0) + 1)
    vals_list = list(lettersCountMap.values())
    print(vals_list)
    try:
        mode = statistics.mode(vals_list)
    except Exception:
        if (len(vals_list) > 2):
            return "NO"
        else:
            return "YES"
    ideal_sum = mode*len(vals_list)
    actual_sum = sum(vals_list)
    if actual_sum == ideal_sum + 1 or actual_sum == ideal_sum - mode + 1 or actual_sum == ideal_sum and not (max(vals_list) - min(vals_list) > 1):
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
