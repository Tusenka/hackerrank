from collections import defaultdict
from functools import cache
from typing import DefaultDict

M = 10 ** 9 + 7

def _build_seq(a:list):
    a.sort()
    if len(a)==2:
        return a[1]-a[0]
    _dp=[[M for _ in range(2)] for _ in range(len(a))]
    _dp[1][1]=a[1]-a[0]
    _dp[2][1]=a[2]-a[1]+_dp[1][1]
    _dp[2][0]=_dp[1][1]

    for i in range( 3, len(a)):
        _dp[i][1]=min(_dp[i-1][1], _dp[i-1][0]) + (a[i]-a[i-1])
        _dp[i][0]=_dp[i-1][1]
    return _dp[-1][1]



if __name__ == '__main__':
    n = int(input().rstrip())
    a = list([int(x) for x in input().rstrip().split()])
    print(_build_seq(a))
