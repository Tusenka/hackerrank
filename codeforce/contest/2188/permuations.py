def solve(n: int):
    p = [-1] * n
    m = n // 2 + 1 if n % 2 else n // 2 + 1
    p[0] = m
    j = 1

    if n % 2:
        for i in range(1, m):
            p[j] = m - i
            p[j + 1] = m + i
            j += 2
    else:
        for i in range(1, m - 1):
            p[j] = m - i
            p[j + 1] = m + i
            j += 2

    if n % 2 == 0:
        p[n - 1] = 1

    return p


t = int(input())

for _ in range(t):
    n = int(input())
    print(*solve(n))
