#!/bin/python3

import os

M=10**5
x=100
x_power2_mod=(2**x)%M

def _power2_mod(n):
    res=1
    while n>=x_power2_mod:
        res=res*x_power2_mod
        n-=x
    if n>0:
        res=res*(2**n % M)
    return res %M
    
def lights(n):
    return (_power2_mod(n)-1)%M
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
