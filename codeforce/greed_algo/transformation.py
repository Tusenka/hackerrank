# https://codeforces.com/problemset/problem/1506/D
from collections import defaultdict


def solve(a: list[int]):
    ah = defaultdict(int)

    for x in a:
        ah[x] += 1

    ac = sorted(ah.values(), reverse=True)
    for i in range(len(ac) - 1):
        j = i + 1
        while ac[i] > 0 and j < len(ac):
            x = min(ac[i], ac[j])
            ac[i] -= x
            ac[j] -= x
            j += 1

    return sum(ac)


t = int(input())

for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))

    print(solve(a))
