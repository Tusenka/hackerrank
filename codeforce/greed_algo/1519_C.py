def solve(s: list, u: list):
    n = len(s)

    a = [[] for _ in range(n)]
    for i in range(n):
        a[u[i] - 1].append(s[i])

    for i in range(n):
        a[i].sort(reverse=True)

    p = [[] for _ in range(n)]

    for i in range(n):
        if not len(a[i]):
            continue
        p[i].append(a[i][0])
        for j in range(1, len(a[i])):
            p[i].append(a[i][j] + p[i][j - 1])

    ans = [0] * n
    for i in range(n):
        for v in p:
            x = (len(v) // (i + 1)) * (i + 1) if len(v) > 0 else 0
            if x > 0:
                ans[i] += v[x - 1]

    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))

    print(*solve(s=s, u=u))
