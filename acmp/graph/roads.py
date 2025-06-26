#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=54&id_problem=676
import dataclasses
import heapq
import sys
from collections import defaultdict, deque

M=10**9

@dataclasses.dataclass()
class Road:
    w: int
    t: int

def _bin_search(f, r):
    l=0

    while r-l>1:
        m=(r+l)//2
        if f(m):
           l=m
        else:
           r=m
    return l


def _min_path(a, n, w):
    d = [M]*n
    queue = [(0, 0)]
    d[0]=0
    visited=[False]*n
    while queue:
        _, curr=heapq.heappop(queue)
        if visited[curr]:
            continue
        visited[curr]=True
        for i, x in a[curr].items():
            if x.w>=w and d[i]>d[curr]+x.t:
                d[i] = x.t+d[curr]
                queue.append((d[i],i))

    return d[-1]<=1440


if __name__ == '__main__':
    n, r = tuple(int(x) for x in input().rstrip().split())
    a=[{} for _ in range(n)]
    _max_w=0

    for _ in range(r):
        i, j, t, w = tuple(int(x) for x in input().rstrip().split())
        w=(w-3*10**6)//100
        _max_w=max(_max_w, w)
        a[i-1][j-1]=Road(w,t)
        a[j-1][i-1]=Road(w,t)

    print(_bin_search(lambda w: _min_path(a, n, w), _max_w+1))

