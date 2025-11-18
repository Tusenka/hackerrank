#https://codeforces.com/contest/2149/problem/C

def solve(a, k):
    am=list(filter(lambda x: x>0, a))
    am.sort()
    a.sort()
    c=0
    if a[0]==k+1:
        return 0
    if len(am)>0  and am[0]==k+1:
        return 0
    if k==0:
       return len(a)-len(am)
    c=1
    l=a[0]
    seq=(l==0)
    for x in a:
        if x>=k:
            return c
        c+=1
        if x!=l+1 and x!=l:
            seq=False
        l=x
    if seq and a[-1]==k-1:
        return 0

    return c


t=int(input())

for _ in range(t):
    n,k=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    print(solve(a,k))


