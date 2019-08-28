# Problem Link
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_count = 0
    max_count = 0
    min_value = scores[0]
    max_value = scores[0]
    for i in range(len(scores)):
        if min_value > scores[i]:
            min_value = scores[i]
            min_count += 1
        if max_value < scores[i]:
            max_value = scores[i]
            max_count += 1
    return [max_count, min_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
