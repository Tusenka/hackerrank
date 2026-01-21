from __future__ import annotations
from functools import cache, reduce

b = 29
b2 = 326
M = 1234567891
M2 = 1234567891


def solve(a: list, k: int):
    count1 = [0] * len(a)

    if a[0] == 1:
        count1[0] = 1
    for i in range(1, len(a)):
        if a[i] == 1:
            count1[i] = 1 + count1[i - 1]
        else:
            count1[i] = count1[i - 1]

    res = int(a[0] == 1)

    for j in range(len(a) - 1, 0, -1):
        if a[j] == 0:
            continue

        if count1[j - 1] == 0 or (j >= k and count1[j - 1] - count1[j - k] == 0):
            res += 1

    return res


t = int(input())

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    a = list(map(int, input()))
    print(solve(a, k))
