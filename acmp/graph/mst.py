#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=55&id_problem=1043
import heapq
import sys

M = 10 ** 9 + 7


def _solve(n, aa: set):
    _imins =list(aa)

    heapq.heapify(_imins)

    visited = [False] * n
    _ans = 0

    while _imins:
        x = heapq.heappop(_imins)

        if visited[x[1]] and visited[x[2]]:
            continue

        visited[x[1]] = True
        visited[x[2]] = True

        _ans += x[0]

    return _ans


if __name__ == '__main__':
    n, m = tuple(int(x) for x in input().rstrip().split())
    aa = set()

    for _ in range(m):
        i, j, v = tuple(int(x) for x in input().rstrip().split())
        aa.add((v, i-1, j-1))

    print(_solve(n, aa))
