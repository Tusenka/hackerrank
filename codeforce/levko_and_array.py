# https://codeforces.com/problemset/problem/360/B
from __future__ import annotations


def bin_search(r, f):
    l = 0

    while r - l > 1:
        mid = r + l // 2
        if f(mid):
            r = mid
        else:
            l = mid
    return r


def check(a: list, x: int, k: int):
    dp = [1] * len(a)

    for i in range(len(a)):
        for j in range(len(a)):
            if abs(a[i] - a[j]) < x * abs(j - i):
                dp[i] = max(dp[i], dp[j] + 1)

    return len(a) - sum(dp) <= k


def solve(a: list, k: int):
    x = max(a) - min(a) + 1

    return bin_search(r=x, f=lambda v: check(a=a, x=v, k=k))


n, k = tuple(map(int, input().rstrip().split()))

a = list([int(x) for x in input().rstrip().split()])

print(solve(a, k))
