#https://codeforces.com/contest/2167/problem/C?locale=en

def _get_imin(a, i):
    for j in range(i+1, len(a)):
        if a[j]<a[i]:
            i=j
    return i

def _try_to_solve(a: list, i:int):
    if i==len(a)-1:
        return

    _imin=_get_imin(a, i)
    _min=a[_imin]

    if _min==a[i]:
       _try_to_solve(a=a, i=i+1)
       return

    if _min%2!=a[i]%2:
       a[i], a[_imin] = a[_imin], a[i]

       _try_to_solve(a=a,i=i+1)
       return


    for j in range(i,len(a)):
        if a[j]%2!=a[i]%2:
            a[i], a[j] = a[j], a[i]
            a[i], a[_imin] = a[_imin], a[i]
            _try_to_solve(a=a,i=i+1)
            return

def solve(a: list[int]):
    _try_to_solve(a=a, i=0)
    return a


t=int(input())
for _ in range(t):
    _ = int(input())
    a=list(map(int,input().split()))
    print(*solve(a))