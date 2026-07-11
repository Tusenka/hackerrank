def dfc(i, c, a, visited):
    if c[i] == 0:
        return 0
    if i in visited:
        return c[i]
    if len(a[i]) == 0:
        return c[i]
    res = 0
    for j in a[i]:
        res += dfc(j, c, a, visited)

    c[i] = min(res, c[i])
    visited[i] = True

    return c[i]


def solve(c, a):
    dp = [0] * len(c)
    visited = {}
    for i in range(len(c)):
        dp[i] = dfc(i, c, a, visited)
    return dp


t = int(input())

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for i in p:
        c[i - 1] = 0
    a = [[]] * n

    for i in range(n):
        a[i] = list(map(lambda x: int(x) - 1, input().split()))[1:]

    print(*solve(c, a))
