#https://codeforces.com/contest/2118/problem/B
from functools import lru_cache

@lru_cache
def _check_bit ( m , x ) :
    return 2 ** x & m

@lru_cache
def _count_1(m):
    _count=0
    while m>0:
        _count+=m & 1
        m=m>>1
    return _count

def _imin(_dp: list):
    _imin=0
    for i in range(len(_dp)):
        if _dp[i]<_dp[_imin]:
           _imin=i
    return _imin

def _solve(a: list, k: int):
    _dp=[_count_1(x) for x in a]
    for i in range(len(_dp)):
        if a[i]%2==0 and k>=1:
           _dp[i]+=1
           k-=1
        if k<1:
            return sum(_dp)
    _sum=sum(_dp)
    _dp = sorted(zip(_dp, a))

    while k>2:
        for i in range(len(_dp)):
            _new_count=_count_1(_dp[i][1]+2)
            if _new_count>_dp[i][0] and k>=2:
                _dp[i]=tuple(_new_count, _dp[i][1]+2)
            if k<2:
                break
        k-=1
    return sum(x[0] for x in _dp)

t=int(input())

for _ in range(t):
    n, k = tuple(int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    print(_solve(a, k))


        
