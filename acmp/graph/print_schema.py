# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=55&id_problem=1045

def conv(i, j):
    return i * 100 + j


def deconv(x):
    return x // 100+1, x % 100+1


def _get_p(p: list, i):
    if p[i] == -1:
        return i
    else:
        p[i] = _get_p(p, p[i])
    return p[i]


def _kraskal(n: int, edges: list):
    p = [-1] * n
    edges.sort()
    _ans = 0
    _count = 0
    _res = []

    for x in edges:
        p1 = _get_p(p, x[1])
        p2 = _get_p(p, x[2])

        if p1 == p2:
            continue

        p[p2] = p1

        if x[0] > 0:
            _count += 1
            _ans += x[0]
            _res.append((*deconv(x[1]), x[0]))

    return _count, _ans, _res


n, m = tuple(map(int, input().rstrip().split()))
edges = list()

for i in range(n):
    a = tuple(map(int, input().rstrip().split()))

    for j in range(m):
        if a[j] == 0:
            if i<n-1:
                edges.append((1, conv(i, j), conv(i + 1, j)))
            if j<m-1:
                edges.append((2, conv(i, j), conv(i, j + 1)))
        if a[j] == 1:
            edges.append((0, conv(i, j), conv(i + 1, j)))
            if j < m - 1:
                edges.append((2, conv(i, j), conv(i, j + 1)))
        if a[j] == 2:
            if i<n-1:
                edges.append((1, conv(i, j), conv(i + 1, j)))
            edges.append((0, conv(i, j), conv(i, j + 1)))
        if a[j] == 3:
            edges.append((0, conv(i, j), conv(i + 1, j)))
            edges.append((0, conv(i, j), conv(i, j + 1)))

ans=_kraskal(n=100 * 100, edges=edges)
print(ans[0], ans[1])

for x in ans[2]:
    print(*x)
