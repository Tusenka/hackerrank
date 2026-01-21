#https://codeforces.com/problemset/problem/478/B
import math


def solve(n:int, m: int):
    if m==1:
        return asum(n-m+1), asum(n-m+1)
    #
    return get_min(n=n, m=m), asum(n - m + 1)

def get_min(n: int, m: int):
    u=math.ceil(n/m)
    l=n//m
    if u==l:
        return asum(u)*m

    
    for i in range(1, n//l):
        if u*i+l*(m-i)==n:
            return asum(u)*i+asum(l)*(m-i)

    assert False



def asum(val:int):
    return (val*(val-1))//2

n,m=tuple(map(int,input().split()))

print(*solve(n,m))