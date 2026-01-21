# https://codeforces.com/group/sNzo7JKQN1/contest/527247/problem/F?locale=ru
M = 10**9


def solve(a: list):
    pass


def floyd(a: list):
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(a[0])):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])

    return max(max(a))


def dfs(a: list, i=0, visited=None, res=None):
    if res is None:
        res = []
    if visited is None:
        visited = set()
    visited.add(i)
    res.append(i)

    for j in a[i]:
        if j in visited:
            continue
        dfs(a=a, i=j, visited=visited, res=res)
    return res


def _cost(c: list, order: list):
    res = 0
    for i in range(len(order) - 1):
        res += c[order[i]][order[i + 1]]
    return res + c[order[-1]][order[0]]


def ring(c: list, r: list):
    order = dfs(r)
    return min(_cost(c, order), _cost(c, list(reversed(order))))


n = int(input())

a = [[M for _ in range(n)] for _ in range(n)]

c = [[0 for _ in range(n)] for _ in range(n)]
r = [set() for _ in range(n)]

for _ in range(n):
    i, j, cij = tuple(map(int, input().split()))
    a[i - 1][j - 1] = 0
    a[j - 1][i - 1] = cij

    c[j - 1][i - 1] = cij
    r[i - 1].add(j - 1)
    r[j - 1].add(i - 1)

print(ring(c, r))
# print(floyd(a))
