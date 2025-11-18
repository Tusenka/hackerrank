from __future__ import annotations
import dataclasses
from functools import cache, reduce

b=29
b2=326
M=1234567891
M2=1234567891


@cache
def bi(i):
    if i==0:
        return 1
    return (bi(i-1)*b)%M

@cache
def b2i(i):
    if i==0:
        return 1
    return (b2i(i-1)*b2)%M2


def _hash(s: str):
    res=0
    for i, x in enumerate(s):
        res+=(bi(i)*(ord(x)-ord('a')+1))%M
    return res%M

def _norm_hash(i1, i2, h):
    if i1>=i2:
       return h
    else:
       return h*bi(i2-i1)%M


def _hash2(s: str):
    res=0
    for i, x in enumerate(s):
        res+=(b2i(i)*(ord(x)-ord('a')+1))%M2
    return res%M2


def _prepare(a):
    return [(_hash(a[:i])) for i in range(len(a))]


def solve(h: list, i: int, j: int, i1: int, j1: int):
    h1=h[j]-h[i-1] if i>0 else h[j]
    h2=h[j1]-h[i1-1] if i1>0 else h[j1]

    return _norm_hash(i1=i,i2=i1, h=h1)==_norm_hash(i1=i1,i2=i,h=h2)



t=int(input())

for _ in range(t):
    i,j, i1,j1=tuple(map(int,input().split()))
    print(solve(h=h, i=i-1, j=j-1, i1=i1-1, j1=j1-1))