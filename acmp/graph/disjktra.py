#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=16&id_topic=21&id_problem=110
import sys

M=10**9+7
def _imin(d: list, visited: list[bool]):
    imin=0
    for i, v in enumerate(d):
        if not visited[i] and d[imin]>v:
            imin=i
    return imin

def _solve(a0: int, a1:int, a: list[tuple]):
    d=[M]*len(a)
    d[a0]=0
    visited=[False]*len(a)
    for _ in range(n):
        imin=_imin(d, visited)
        visited[imin]=True
        for i, x in enumerate(a[imin]):
            d[i] = min(d[i], d[imin]+x)
    return d[a1]
                


if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    n, a0, a1 = tuple(int(x) for x in input().rstrip().split())
    a=[ ()  for _ in range(n)]
    for i in range(n):
        a[i] = tuple(int(x) if x!='-1' else M for x in input().rstrip().split())
    print(_solve(a0-1, a1-1, a))
