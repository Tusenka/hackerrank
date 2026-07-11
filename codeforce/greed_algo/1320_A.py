# https://codeforces.com/problemset/problem/1320/A

from mypy.checkpattern import defaultdict


def solve(a: list[int]):
    res = defaultdict(int)
    h = [a[i] - i for i in range(len(a))]

    for i in range(len(h)):
        res[h[i]] += a[i]

    return max(res.values())


n = int(input())
a = list(map(int, input().split()))
print(solve(a))
