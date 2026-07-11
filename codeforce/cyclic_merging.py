# https://codeforces.com/contest/2165/problem/A
M = 10**9


def solve(a: list):
    l = len(a)
    res = 0
    _d = set()

    for i in range(l - 1):
        res += max(a[i], a[i + 1])
    res += max(a[0], a[-1])
    res -= max(a)
    # while l:
    #     l-=1
    #     imin=am[-l-1][1]
    #     j=imin+1 if imin<len(a)-1 else 0
    #     i=imin-1 if imin>0 else len(a)-1
    #
    #     _min=min(a[i], a[j])
    #     res+=_min
    #     _d.add(imin)
    #     for x in _d:
    #         a[x]=_min

    return res


t = int(input())
for _ in range(t):
    _ = int(input())
    a = list(map(int, input().split()))
    print(solve(a))
