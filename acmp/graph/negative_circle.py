from copy import deepcopy

M = 100000


def floyd(a: list[list]):
    dp = deepcopy(a)
    p = [[i for _ in range(len(a))] for i in range(len(a))]

    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                if dp[i][k] < M and dp[k][j] < M:
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        p[i][j] = p[k][j]
                        dp[i][j] = dp[i][k] + dp[k][j]

    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                if dp[i][k] < M and dp[k][j] < M:
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        p[i][j] = p[k][j]
                        dp[i][j] = dp[i][k] + dp[k][j]
                        return dp, p
    return dp, p


def _asum(a: list[list]):
    dp = deepcopy(a)
    p = [[i for _ in range(len(a))] for i in range(len(a))]

    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                if dp[i][k] < M and dp[k][j] < M:
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        p[i][j] = p[k][j]
                        dp[i][j] = dp[i][k] + dp[k][j]

    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                if dp[i][k] < M and dp[k][j] < M:
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        p[i][j] = p[k][j]
                        dp[i][j] = dp[i][k] + dp[k][j]
                        return dp, p
    return dp, p


def recovery_path(p, i, j):
    yield j + 1

    x = p[i][j]

    while i != x:
        yield x + 1
        x = p[i][x]

    yield i + 1


def find_circle(dp, p):
    for i in range(len(dp)):
        if dp[i][i] < 0:
            return list(reversed(list(recovery_path(p, i, i))))
    return []


n, m = tuple(int(x) for x in (input().rstrip()))
a = [[M for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = [int(x) for x in input().rstrip().split()]

dp, p = floyd(a)
res = find_circle(dp, p)
if res:
    print("YES")
    print(len(res))
    print(*res)
else:
    print("NO")
