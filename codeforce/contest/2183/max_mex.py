# https://codeforces.com/contest/2183/problem/B


def solve(a: list, k: int):
    return min(mex(a), k - 1)


def mex(a: list):
    _m = max(a)
    vals = [False] * (_m + 1)
    for x in a:
        vals[x] = True

    for i in range(len(vals)):
        if not vals[i]:
            return i + 1 if i else 0
    return _m + 1


t = int(input())

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    print(solve(a, k))
