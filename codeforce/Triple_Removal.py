#https://codeforces.com/contest/2152/problem/C
from copy import copy

def prepare(a):
    pass

def solve(a:list, l, r):
    if len([x for x in a[l: r+1] if x==0])%3:
        return -1
    for i in range(l,r-1):
        if a[i]==a[i+1]:
            return (r-l+1)//3

    return (r-l+1)//3+1

t = int(input().rstrip())

for _ in range(t):
    _,k=tuple(map(int,input().rstrip().split()))
    a = list(map(int, input().rstrip().split()))

    for i in range(k):
        l, r = tuple(map(int, input().rstrip().split()))
        print(solve(a, l-1, r-1))