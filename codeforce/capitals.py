# https://codeforces.com/problemset/problem/219/D?mobile=true&locale=en
import heapq
from collections import deque

D = 20000
M = 10**9 + 7


def _get_capitals(a: list):
    n = len(a)
    visited = set()
    dp = [M for _ in range(n)]
    dp[0] = _ford_bellman(a)

    am = [[M for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for x in a[i]:
            am[i][x[1]] = x[0]

    q = deque()
    for i in a[0]:
        q.append((i[0], 0, i[1]))

    while q:
        x = q.popleft()

        if x in visited:
            continue

        visited.add(x)
        dp[x[2]] = (
            dp[x[1]] - 1
            if x[0] == 1
            else dp[x[1]]
            if am[x[2]][x[1]] == am[x[1]][x[2]] == 0
            else dp[x[1]] + 1
        )

        for i in a[x[2]]:
            q.append((i[0], x[2], i[1]))

        for i in a[x[2]]:
            q.append((i[0], x[2], i[1]))

    _min = min(dp)

    return _min, [i + 1 for i in range(n) if dp[i] == _min]


def _ford_bellman(a: list):
    n = len(a)
    dp = [M for _ in range(n)]
    dp[0] = 0

    edges = [(0, 0, 0)]
    for i, x in enumerate(a):
        for e in x:
            edges.append((e[0], i, e[1]))

    for _ in range(n - 1):
        for x in edges:
            if x[0] == 0:
                dp[x[2]] = max(0, min(dp[x[2]], dp[x[1]] - 1))
            else:
                dp[x[2]] = max(0, min(dp[x[2]], dp[x[1]] + 1))

    return sum(dp)


if __name__ == "__main__":
    n = int(input().rstrip())
    aa = [set() for _ in range(n)]

    for _ in range(n - 1):
        i, j = tuple(int(x) for x in input().rstrip().split())
        aa[i - 1].add((0, j - 1))

    for i in range(n):
        for x in aa[i]:
            j = x[1]
            if (0, i) not in aa[j]:
                aa[j].add((1, i))

    res = _get_capitals(aa)
    print(res[0])
    print(*res[1])
