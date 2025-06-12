from collections import defaultdict
from functools import cache
from typing import DefaultDict

M = 10 ** 9 + 7

def _get_value(a:list):
    if len(a)==2:
        return min(a[0][0]+ a[1][0], a[0][1])
    _dp=[[M for _ in range(4)] for _ in range(len(a))]
    _dp[0][1]=a[0][0]
    _dp[0][2]=a[0][1]
    _dp[0][3]=a[0][2]
    for i in range(1, len(a)):
        _dp[i][0]=min([_dp[i-k][k+1] for k in range(1, min(i, 2)+1)])
        for k in range(1, 4):
            _dp[i][k]=min(_dp[i-1][0], _dp[i-1][1])+a[i][k-1]
    return min(_dp[-1][0], _dp[-1][1])


t = int(input().rstrip())
a=[]
for t_itr in range(t):
    row = tuple([int(x) for x in input().rstrip().split()])
    a.append(row)

print(_get_value(a))
