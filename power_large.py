#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
M=10**9 +7
_pows_of_two=[1,2,4]


def _pow_of_two(n):
    global _pows_of_two
    if n>len(_pows_of_two)-1:
        for i in range(len(_pows_of_two)-1, n+2):
            _pows_of_two.append((_pows_of_two[i]*2))
    return _pows_of_two[n]


def _pow_of_value(a, i):
    return a**_pow_of_two(i) % M    


def solve(a, b):
    res=1
    a=int(a)
    b=int(b)
    for i, v in enumerate(reversed(bin(b))):
        if v=='1':
           res=res*_pow_of_value(a, i) % M
    return res % M

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
