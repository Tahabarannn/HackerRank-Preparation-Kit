#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    l = Counter(s[:n//2])
    r = Counter(s[n//2:])

    return len(list((l - r).elements()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
