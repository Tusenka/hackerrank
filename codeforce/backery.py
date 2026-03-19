# https://codeforces.com/group/sNzo7JKQN1/contest/527247/problem/F?locale=ru
M = 10**9


def solve(a: list, p: set):
    for i, row in enumerate(a):
        for j in range(len(row)):
            if j in p:
                a[i][j] = M

    _min = M
    for i in p:
        _min = min(min(a[i]), _min)

    return _min


n, m, k = tuple(map(int, input().rstrip().split()))

a = [[M for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, x = tuple(map(int, input().split()))

    a[i - 1][j - 1] = x
    a[j - 1][i - 1] = x

p = set(int(i) - 1 for i in input().rstrip().split())

if k == 0:
    print(-1)
    exit()

res = solve(a, p)
print(res if res < M else -1)
# print(floyd(a))
