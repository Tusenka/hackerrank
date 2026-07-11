from collections import defaultdict


def solve(a: list[int], b: list[int], c: list[int], h: int):
    hash = defaultdict(int)

    for x in range(len(b)):
        hash[b[x]] += c[x]
        if hash[b[x]] + a[b[x]] > h:
            # reset
            hash = defaultdict(int)
    return [a[i] + hash[i] for i in range(len(a))]


t = int(input())

for _ in range(t):
    n, m, h = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [0] * m
    c = [0] * m
    for i in range(m):
        b[i], c[i] = tuple(map(int, input().split()))
        b[i] -= 1

    print(*solve(a=a, b=b, c=c, h=h))
