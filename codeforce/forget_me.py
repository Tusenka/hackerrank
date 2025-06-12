#https://codeforces.com/contest/2115/problem/D
from functools import lru_cache, reduce
import math

@lru_cache
def _xor(p, q):
    return math.gcd(p, q)

@lru_cache()
def _check_bit ( m , x ) :
    return 2 ** x & m


@lru_cache
def _count_1(m, n):
    return len([1 for x in range(n) if _check_bit ( m , x )])

def _equal(q:list, _min):
    return all(x==_min for x in q)

def _equality(q: list):
    return len(q)-len(set(q))

def _eval_r(a: list, b: list, c:list, n:int):
    x=reduce(lambda x,y: x^y, a)
    b=[b[i]^a[i] for i in range(n)]
    for i in range(n-1, -1, -1):
        new_x=x^b[i]
        if c[i]==1 and new_x>x:
            x=new_x
        elif new_x<x:
            x=new_x
    return x


t=int(input())
for _ in range(t):
    _=input()
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input()]
    print(_eval_r(a, b, c, len(a)))

t=int(input())
for _ in range(t):
    _=input()
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input()]
    print(_eval_r(a, b, c, len(a)))
