# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=55&id_problem=1043
import heapq

D = 20000

M = 10 ** 9 + 7


def _get_p(p: list, i):
    if p[i] == -1:
        return i
    else:
        p[i] = _get_p(p, p[i])

    return p[i]


def _kraskal(n: int, _imins: list, ignore=(-1, -1)):
    p = [-1] * n
    _ans = 0
    edges = []

    _imins.sort()

    for i, x in enumerate(_imins):

        if x == ignore:
            continue

        x1 = x[1] // D
        x2 = x[1] % D
        p1 = _get_p(p, x1)
        p2 = _get_p(p, x2)
        if p1 == p2:
            continue

        p[p2] = p1

        edges.append(x)
        _ans += x[0]

    pp=sorted([_get_p(p, i) for i in range(len(p))])

    if not all(x==pp[0] for x in pp[1:]):
       _ans+=M

    return _ans, edges

if __name__ == '__main__':
    n, m = tuple(int(x) for x in input().rstrip().split())
    aa = [()] * m

    for t in range(0,m, 1):
        i, j, v = tuple(int(x) for x in input().rstrip().split())
        aa[t] = (v, (i - 1) * D + (j - 1))

    _ans, _edges = _kraskal(n, aa)
    print(_ans, end=' ')
    s2 = min([_kraskal(n, aa, ignore=i) for i in _edges])
    print(s2[0])
