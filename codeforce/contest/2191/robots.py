from collections import defaultdict


def bin_search(end, f):
    start = 0
    while start < end:
        mid = (start + end) // 2
        if f(mid):
            end = mid
        else:
            start = mid + 1

    return start


def find_left_right(x, b) -> list[int]:
    if b[-1] < x:
        return [1, 10**9]
    i = bin_search(end=len(b), f=lambda i: b[i] >= x)

    return [x - b[i - 1], b[i] - x] if i > 0 else [10**9, b[i] - x]


def solve(a, b, c):
    hash_a = dict()
    a.sort()
    b.sort()

    for x in a:
        for i in range(x, -1, -1):
            hash_a[x] = find_left_right(x, b)
    ans = []
    for x in c:
        for r in hash_a.values():
            r[0] += x
            r[1] -= x
        keys = set(hash_a.keys())
        for i in keys:
            if hash_a[i][0] <= 0 or hash_a[i][1] <= 0:
                del hash_a[i]

        ans.append(len(hash_a.keys()))

    return ans


t = int(input())

for _ in range(t):
    n, m, k = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [-1 if x == "L" else 1 for x in input()]

    print(*solve(a, b, c))
