#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def is_valid(a, b, c):
    if a < b+c and b < c+a and c < a+b:
        return True
    else:
        return False


def maximumPerimeterTriangle(sticks):
    res = [-1]
    sticks = sorted(sticks, reverse=True)

    print(sticks)

    for ind in range(2, len(sticks)):
        for jnd in range(1, ind):
            for knd in range(0, jnd):
                print("checking {} {} {}".format(
                    sticks[ind], sticks[jnd], sticks[knd]))
                if is_valid(sticks[ind], sticks[jnd], sticks[knd]):
                    print("valid")
                    res = (sticks[ind], sticks[jnd], sticks[knd])
                    return res

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
