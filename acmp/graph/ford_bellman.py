from itertools import product

M = 100000


def ford_bellman(a: list):
    dp = [M] * len(a)
    dp[0] = 0
    p = [i for i in range(len(a))]
    es = [
        (i, j, a[i][j]) for i, j in product(range(len(a)), range(len(a))) if a[i][j] < M
    ]

    for k in range(len(a) - 1):
        for e in es:
            if dp[e[1]] > dp[e[0]] + e[2]:
                dp[e[1]] = dp[e[0]] + e[2]
                p[e[1]] = e[0]

    for e in es:
        if dp[e[1]] > dp[e[0]] + e[2]:
            p[e[1]] = e[0]
            return p, e[1]

    return p, None


def recovery_path(p, j):
    x = p[j]

    while j != x:
        yield x
        x = p[x]

    yield j


def find_circle(p, i):
    p = list(recovery_path(p, i))

    for j, x in enumerate(p):
        if x == i:
            return [i] + p[: j + 1]

    return []


n = int(input().rstrip())
a = [[] for _ in range(n)]

for i in range(n):
    a[i] = tuple(int(x) for x in input().rstrip().split())

p, i = ford_bellman(a)

if i is not None:
    print("YES")
    ans = [x + 1 for x in reversed(find_circle(p, i))]
    print(len(ans))
    print(*ans)

else:
    print("NO")
