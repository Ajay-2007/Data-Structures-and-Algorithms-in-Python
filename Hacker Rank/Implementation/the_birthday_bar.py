# Problem Link
# https://www.hackerrank.com/challenges/the-birthday-bar/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # see that some of s[i:m] is equal to d then count 
    # how much total squares are possbile
    count = 0
    for i in range(len(s)):
        if m+i <= len(s):
            a = sum(s[i:m+i])
            if a == d:
                count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
