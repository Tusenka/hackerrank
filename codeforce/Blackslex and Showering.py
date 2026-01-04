# https://codeforces.com/contest/2179/problem/B?locale=en

def solve(a: list[int]):
    _imax=0 if abs(a[1]-a[0])>abs(a[-1]-a[-2]) else len(a)-1
    _last=abs(a[_imax+1]-a[_imax]) if _imax==0 else abs(a[_imax]-a[_imax-1])
    for i in range(1, len(a)-1):
        diff=abs(a[i]-a[i+1])+abs(a[i]-a[i-1])-abs(a[i+1]-a[i-1])
        if diff>_last:
           _imax=i
           _last=diff

    _ans=0
    for i in range(1, len(a)-(_imax==len(a)-1)):
        if i!=_imax and i!=_imax+1:
            _ans+=abs(a[i]-a[i-1])
        if i==_imax and len(a)-1>i:
           _ans+=abs(a[i+1]-a[i-1])
    return _ans



t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))
    print(solve(a))