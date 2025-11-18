
def solve(p, x):
    _imin=min((v,i) for i,v in enumerate(p))[1]
    _imax=max((v,i) for i,v in enumerate(p))[1]
    if x[0] or x[-1] or x[_imin] or x[_imax]:
        return []
    if _imin<_imax:
        return [(1,_imin+1),(_imin+1, _imax+1),(_imax+1, len(p))]
    else:
        return [(1, _imax+1), (_imax+1, _imin+1), (_imin+1, len(p))]

t=int(input())

for _ in range(t):
    n=int(input())
    p=list(map(int, input().split()))
    x=list(map(int, input()))
    ans=solve(p,x)

    if not ans:
        print(-1)
    else:
        print(len(ans))
        for x in ans:
            print(*x)