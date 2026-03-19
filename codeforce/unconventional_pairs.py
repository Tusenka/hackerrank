# https://codeforces.com/contest/2149/problem/A


def solve(a: list):
    a.sort()
    _max = 0
    for i in range(0, len(a) - 1, 2):
        _max = max(_max, abs(a[i] - a[i + 1]))

    return _max


t = int(input())

for _ in range(t):
    _ = input().split()
    a = list(map(int, input().split()))

    print(solve(a))
