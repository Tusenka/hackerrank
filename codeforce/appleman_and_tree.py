# https://codeforces.com/problemset/problem/461/B?locale=en
from __future__ import annotations

from collections import deque
from functools import reduce


def check(a: list, x: int, k: int):
    dp = [1] * len(a)

    for i in range(len(a)):
        for j in range(len(a)):
            if abs(a[i] - a[j]) < x * abs(j - i):
                dp[i] = max(dp[i], dp[j] + 1)

    return len(a) - sum(dp) <= k


def _solve(p: list, colors: list):
    leafs = [i for i in range(len(p)) if i not in set(p)]
    dp = [[0 for _ in range(2)] for _ in range(len(p))]
    childs = [set() for _ in range(len(p))]

    for i, x in enumerate(p):
        childs[x].add(i)

    for l in leafs:
        if colors[l] == 1:
            dp[l][1] = 1
            dp[l][0] = 0
        else:
            dp[l][0] = 1
            dp[l][1] = 0

    q = deque()
    q.extend(p[l] for l in leafs)

    while q:
        x = q.popleft()
        if p[x] != -1:
            q.append(p[x])

        if colors[x] == 1:
            dp[x][0] = 0
            dp[x][1] = reduce(
                lambda x, y: x * y, [max(dp[c][0], 1) for c in childs[x]], 1
            )

        else:
            dp[x][0] = reduce(lambda x, y: x * y, [dp[c][0] for c in childs[x]], 1)
            dp[x][1] = 0
            for bc in childs[x]:
                dp[x][1] += dp[bc][1] * reduce(
                    lambda x, y: x * y,
                    [max(dp[c][0], 1) for c in childs[x] if c != bc],
                    1,
                )

    return dp[0][1]


n = int(input().rstrip())

p = [-1] + list([int(x) for x in input().rstrip().split()])
colors = list([int(x) for x in input().rstrip().split()])

print(_solve(p, colors))
