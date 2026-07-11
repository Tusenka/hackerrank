from functools import lru_cache


@lru_cache
def _cut_ribon(a: int, b: int, c: int, n: int):
    if n==a: return 1
    if n==b: return b//a if b%a==0 else 1
    if n==c:
        _count=max(_cut_ribon(a, b, c, n-a), _cut_ribon(a, b, c, n-b), 1)
        return _count+1 if _count>0 else 1
    if n<a:
        return 0
    #
    _dp=[-M]*n
    for i in range
    #_dp[a]=1
    #_dp[b] = b//a if b%a==0 else 1
    #_dp[c] = c//a if c%a==0 else c//b if c%b==0 else 1
    _count=max(_cut_ribon(a, b, c, n-a), _cut_ribon(a, b, c, n-b), _cut_ribon(a,b,c,n-c))
    return _count+1 if _count>0 else 0

n,a,b,c=map(int,input().split())
a,b,c=tuple(sorted([a, b, c]))
print(_cut_ribon(a,b,c,n))



