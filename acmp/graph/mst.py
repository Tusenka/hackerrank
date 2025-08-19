# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=55&id_problem=1043
import heapq

D = 20000

M = 10 ** 9 + 7


def _prieme(n: int, a: list):
    am = [[] for _ in range(n)]

    for x in a:
        am[x[1]].append((x[0], x[2]))
        am[x[2]].append((x[0], x[1]))

    _imins = []
    visited = [False] * n
    visited[0] = True

    for x in am[0]:
        heapq.heappush(_imins, x)

    _ans = 0
    while _imins:
        x = heapq.heappop(_imins)

        if visited[x[1]]:
            continue

        visited[x[1]] = True

        for e in am[x[1]]:
            heapq.heappush(_imins, e)

        _ans += x[0]

    return _ans


def _get_p(p: list, i):
    if p[i] == -1:
        return i
    else:
        p[i] = _get_p(p, p[i])

    return p[i]


def _kraskal(n: int, _imins: list):
    p = [-1] * n
    _imins.sort()
    _ans = 0

    for x in _imins:
        x1 = x[1] // D
        x2 = x[1] % D
        p1 = _get_p(p, x1)
        p2 = _get_p(p, x2)

        if p1 == p2:
            continue

        p[p2] = p1

        _ans += x[0]

    return _ans


def _kraskal2(n: int, _imins: list):
    p = [-1] * n
    h = [0] * n
    _imins.sort()
    _ans = 0

    for x in _imins:
        x1 = x[1] // D
        x2 = x[1] % D
        p1 = _get_p(p, x1)
        p2 = _get_p(p, x2)

        if p1 == p2:
            continue

        if h[p1] > h[p2]:
            p[p1] = p2

        elif h[p2] > h[p1]:
            p[p2] = p1

        else:
            p[p2] = p1
            h[p1] += 1

        _ans += x[0]

    return _ans


if __name__ == '__main__':
    n, m = tuple(int(x) for x in input().rstrip().split())
    aa = [()] * m

    for t in range(m):
        i, j, v = tuple(int(x) for x in input().rstrip().split())
        aa[t] = (v, (i - 1) * D + (j - 1))

    print(_kraskal2(n, aa))
