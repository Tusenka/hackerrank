#!/bin/python3

import math
import os

_dp = []
MOD = 10 ** 8 + 7


def _get_dp(n, m, i):
    if 2 * i > n:
        i = n
    global _dp
    if _dp[m][i] > 0:
        return _dp[m][i]
    else:
        raise KeyError(f"Can't build for key {m} i {i}")


def _set_dp(n, m, i, value):
    if 2 * i > n:
        i = n
    global _dp
    _dp[m][i]=value


def _next_letter(n, m, i=-1):
    global MOD
    if n % 2 == 0:
        k = int(n / 2)
    else:
        k = math.ceil(n / 2)
    if i == -1:
        return sum([_next_letter(n, m, j) for j in range(n-k, n + 1)] ) % MOD + _next_letter(n, m, n)*k
    if m <= 2:
        # print(f"Last letter could be only last half i {i} x{x}")
        if i * 2 > n:
            # print(f"{i} is last half could be any letter followd by, ans {k}")
            _set_dp(n, m, i, k)
            return k
        else:
            ans = (max(n - 2 * i + 1, 0) if 2 * i > n - k else k) % MOD
            # print(f"{i} is first half could be letter check after {n-2*i} becasue 2*(n-k)>=i {2*(n-k)>i} for k{k} and n {n}  ans {ans}")
            _set_dp(n, m, i, ans)
            return ans
    if i * 2 > n:
        ans = k * _get_dp(n, m - 1, i)
        # print(f"k {k} i {i} is greater than {n} second half sum {ans} x {x}")
        for j in range(1, n - k + 1):
            # print(f"check letter j {j} for {i} which is in first_half x {x}")
            ans += _get_dp(n, m - 1, j) % MOD
        _set_dp(n,m,i,ans)
        return ans
    else:
        ans = 0
        # print(f"k {k} i {i} is less than {n} x {x}")
        for j in range(2 * i, n + 1):
            # print(f"check letter j {j} which is greater than {i} x {x}")
            ans += _get_dp(n, m - 1, j) % MOD
        _set_dp(n,m,i,ans)
        return ans

def pre_build_letters(n, m):
    for i in range(2, m+1):
        _next_letter(n, i, -1)

def alienLanguages(n, m):
    global _dp
    _dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    pre_build_letters(n, m)
    return sum([_get_dp(n, m, i) for i in range(1, n + 1)]) % MOD
    # Write your code here
f=open("test.txt")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] if "OUTPUT_PATH" in os.environ else "test_result.log", 'w')

    t = int(f.readline().strip())

    for t_itr in range(t):
        ( n, m )= tuple([int(x) for x in f.readline().rstrip().split()])
        result=alienLanguages(n, m)
        print(result)
        fptr.write(str(result) + '\n')
    fptr.close()