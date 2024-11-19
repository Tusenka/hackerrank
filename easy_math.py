#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER x as parameter.
#

_numbers={1: [4], 2: [40, 44]}
_four_ten_powers_=[4, 44, 444, 4444, 44444, 444444 ]
_ten_powers=[1, 10, 100, 1000, 10000 ]

def _ten_power(n):
    global _ten_powers
    if n>len(_ten_powers)-1:
        for i in range(len(_ten_powers)-1, n+2):
           _ten_powers.append(_ten_powers[i]*10)
    
def _four_ten_power(n):
    global _four_ten_powers_
    n=n-1
    if n>len(_four_ten_powers_)-1:
        for i in range(len(_four_ten_powers_)-1, n+1):
            _four_ten_powers_.append(_four_ten_powers_[i]+_ten_power(i+1)*4)
    return _four_ten_powers_[n]
                    
                    
def _get_number(a, b):
    res=_four_ten_power(a)
    res*=_ten_power(b)
    return int(res)
        
        
def _transform_result(n):
    a=str(n).count('4')
    b=str(n).count('0')
    return a * 2 + b
                
def _next_number_chain(n):
    if n in _numbers:
       yield from _numbers[n]
    else:
        _numbers[n]=[]
        for a in range(1, n+1):
            b=n-a
            num=_get_number(a, b)
            _numbers[n].append(num)
            yield num


def _next_number(n_begin):
    while True:
        for num in _next_number_chain(n_begin):
            yield num
        n_begin+=1

def _is_divisible(x, y):
    return x%y ==0

def solve(x):
    n_begin=len(str(x))
    for xy in _next_number(n_begin):
        if _is_divisible(xy, x):
            return _transform_result(xy)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        x = int(input().strip())

        result = solve(x)

        fptr.write(str(result) + '\n')

    fptr.close()
