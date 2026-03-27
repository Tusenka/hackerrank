def solve(a: list, b: list, m: int):
    return _solve([m]+a,b)

def _solve(a: list, b: list):
    a.sort()
    b.sort()

    _c=0
    ai=0
    bi=0
    n = len(a)

    while ai<n:
        while a[ai]>=b[bi]:
            n-=1
            bi+=1
            _c+=1

        ai+=1
        bi+=1

    return _c


t=int(input())

for _ in range(t):
    n,m=tuple(map(int,input().split()))
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    print(solve(a, b, m))