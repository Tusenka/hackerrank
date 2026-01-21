# https://codeforces.com/contest/2182/problem/C


def solve(a: list[int], b: list[int], c: list[int]):
    n = len(a)
    a = a + a
    b = b + b
    c = c + c
    d1 = 0
    d2 = 0

    for i in range(n):
        for ii in range(i, n + i):
            if b[ii - i] - a[ii] <= 0:
                break
        else:
            d1 += 1

    for i in range(n):
        for ii in range(i, n + i):
            if b[ii - i] - c[ii] >= 0:
                break
        else:
            d2 += 1

    return d1 * d2 * n


t = int(input())

for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    print(solve(a, b, c))
