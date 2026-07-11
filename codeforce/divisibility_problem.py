# https://codeforces.com/contest/2140/problem/B
from math import log, sqrt


def solve(a):
    if a % 2 == 0:
        return a // 2
    for y in range(10, a // 2, 2):
        res = int(str(a) + str(y))
        if res % (a + y) == 0:
            # return y
            print(y, a / y if y > 0 else 0, res, log(y, 10) if y > 0 else 0, log(a, 10))
    return None


t = int(input().rstrip())

for _ in range(t):
    x = int(input().rstrip())
    print(solve(x))
