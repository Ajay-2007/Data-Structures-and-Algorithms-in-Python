# Problem Link
# https://www.hackerrank.com/challenges/migratory-birds/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    type_arr = [[i, 0] for i in range(1, 6)]
    for i in range(len(arr)):
        if arr[i] == type_arr[0][0]:
            type_arr[0][1] += 1
        if arr[i] == type_arr[1][0]:
            type_arr[1][1] += 1
        if arr[i] == type_arr[2][0]:
            type_arr[2][1] += 1
        if arr[i] == type_arr[3][0]:
            type_arr[3][1] += 1
        if arr[i] == type_arr[4][0]:
            type_arr[4][1] += 1
    ans = sorted(type_arr, key = lambda kv : (kv[1]), reverse=True)
    return ans[0][0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
