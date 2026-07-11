from typing import Callable

def bin_searh(l: int, r: int, v: int, f: Callable[[int], bool]):
    while l+1<r:
        m=(l+r)//2

        if f(m):
           l=m
        else:
           r=m

    return l

def is_palindrom(a: int)->bool:
    a=str(a)
    if len(a)==1:
        return True

    for i in range(len(a)//2):
        if a[i]!=a[-i-1]:
           return False

    return True

def solve(n: int):
    if n<12:
        return [n,0] if is_palindrom(n) else [-1]

    b=bin_searh(l=0, r=(n//12)+1, v=n, f=lambda x: 12*x<=n )*12
    a=n-b

    while a>=0 and b>=0:
        if is_palindrom(a):
            return [a,b]
        b-=12
        a+=12

    return [-1]


t=int(input())

for _ in range(t):
    n=int(input())
    print(*solve(n))
