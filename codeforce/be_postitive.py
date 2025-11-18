#https://codeforces.com/contest/2149/problem/A

def solve(a:list):
    c=0
    n=0
    for x in a:
        if x==0:
            c+=1
        if x==-1:
           n+=1
    if n%2==0:
        return c
    else:
        return c+2


t = int(input())

for _ in range(t):
    _=input().split()
    a=list(map(int,input().split()))

    print(solve(a))