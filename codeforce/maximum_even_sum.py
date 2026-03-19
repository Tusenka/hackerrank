# https://codeforces.com/contest/2137/problem/C
from math import sqrt


def solve(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return 2 + a * b // 2
    if a % 2 == 0 and b % 2 == 1:
        return -1
    if a % 2 == 1 and b % 2 == 0 and b % 4 > 0:
        return -1
    if a % 2 == 1 and b % 4 == 0:
        return a * 2 + b // 2

    if a % 2 == 1 and b % 2 == 1:
        return a * b + 1

    return -1


t = int(input().rstrip())

for _ in range(t):
    a, b = tuple(map(int, input().rstrip().split()))
    print(solve(a, b))
