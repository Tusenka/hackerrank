#https://codeforces.com/contest/2116/problem/B
from functools import lru_cache
import math

@lru_cache
def _gcd(p, q):
    return math.gcd(p, q)

@lru_cache
def _agcd(q: tuple):
    return math.gcd(*q)

@lru_cache
def _agcdm(q:tuple, m, n):
    return _agcd( tuple( q[x] for x in range(n) if _check_bit ( m , x ) ) )


def _check_bit ( m , x ) :
    return 2 ** x & m


@lru_cache
def _count_1(m, n):
    return len([1 for x in range(n) if _check_bit ( m , x )])

def _equal(q:list, _min):
    return all(x==_min for x in q)
    #return len(set(q))==len(q)

def _equality(q: list):
    return len(q)-len(set(q))

def _eval_r(q: tuple):
    _x=_agcd(q)
    _dp=[len(q)]*len(q)
    if _x in set(q):
        return len([x for x in q if x!=_x])
    for i in range(len(q)):
        for j in range(2**len(q)):
            if (2**i)&j and _agcdm(q, j, len(q))==_x:
                _dp[i]=min(_dp[i], _count_1(j, len(q))-1)
    return len(q)-1+min(_dp)

t=int(input())
for _ in range(t):
    _=input()
    q = tuple(int(x) for x in input().split())
    print(_eval_r(q))


def _eval_r(q: list):
    _min=0
    M=10**9
    for x in q:
        _min=_gcd(_min, x)
    if _min in set(q):
        return len([x for x in q if x!=_min])-1
    for i in range(len(q)):
        q[i]//=_min
    m=max(q)
    _dp= [ M ] * (m + 1)
    for x in q:
        _dp[x]=0
    for x in range(m, 0, -1):
        for y in q:
            _dp[_gcd(x,y)]=min(_dp[_gcd(x,y)], _dp[x]+1)
    return max(_dp[1]-1,0)+len(q)
          
    
    

