# https://codeforces.com/contest/2136/problem/B
from collections import deque


def solve(k, a):
    p = deque([i + 1 for i in range(len(a))])
    res = [-1] * len(a)
    j = 0
    while p:
        for i in range(k - 1):
            if not a:
                return res
            res[j] = a.pop()[1]
            j += 1
        if a:
            res[j] = a[0][1]
            del a[0]
    return res


t = int(input().rstrip())

for _ in range(t):
    _, k = tuple(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip()))
    for i, x in enumerate(arr):
        arr[i] = (x, i)
    print(solve(k, arr))
