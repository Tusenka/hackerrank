# https://codeforces.com/contest/2143/problem/C


def topology_sort(a, i, res=None, visited=None):
    if visited is None:
        visited = set()
    if res is None:
        res = []

    visited.add(i)

    for x in a[i]:
        if x in visited or x < 0:
            continue
        topology_sort(a=a, i=x, res=res, visited=visited)

    res.append(i)
    return res


def solve(a, p):
    i = [i for i in range(len(p)) if p[i] == -1][0]
    res = topology_sort(a, i)
    res = [x + 1 for x in res]
    return res


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())

    a = [set() for _ in range(n)]
    p = [-1] * n
    for _ in range(n - 1):
        i, j, x, y = tuple(map(int, input().rstrip().split()))
        if x > y:
            p[j - 1] = i - 1
            a[i - 1].add(j - 1)

        else:
            p[i - 1] = j - 1
            a[j - 1].add(i - 1)

    print(*solve(a=a, p=p))
