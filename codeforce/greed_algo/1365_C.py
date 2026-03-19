from collections import defaultdict


def solve(a: list, b: list):
    ah = defaultdict(int)

    for i, x in enumerate(a):
        ah[x - i] += 1

    bh = defaultdict(int)

    for i, x in enumerate(b):
        bh[x - i] += 1

    return min(max(ah.values()), max(bh.values()))


_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(a, b))
