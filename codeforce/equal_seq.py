#https://codeforces.com/contest/2118/problem/A
from functools import lru_cache



def _solve(n: int, k: int):
    s=''
    for i in range(k):
        s+='1'
    for i in range(k, n):
        s+='0'
    return s

t=int(input())
for _ in range(t):
    n, k = tuple(int(x) for x in input().split())
    print(_solve(n,k))


        
