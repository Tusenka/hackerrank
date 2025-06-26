#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=54&id_problem=676
import dataclasses
import heapq
import sys
from collections import defaultdict

M=10**9
class Trip:
    def __init__(self, n):
        self.d = [[[] for _ in range(n)] for _ in range(25)]
        self.n=n

    def add_point(self, to, td, n):
        for i in range(to+1):
            self.d[i][n].append(td)

    def get_point(self, start, n):
        return min(self.d[start][n]) if len(self.d[start][n])>0 else M

    def get_points(self, start):
        for i in range(self.n):
            if  len(self.d[start][i])>0:
                yield min(self.d[start][i]), i

    def __repr__(self):
        return f'Trip {self.d}'
        

def _min_path(a, x, y):
    d = {x: 0}
    queue = [(x, 0)]

    while queue:
        i, start=queue.pop(0)
        for td, j in a[i].get_points(start=start):
            queue.append((j, td))
            if j not in d:
                d[j]=td
            else:
                d[j]=min(d[j], td)

    return d.get(y, -1)


if __name__ == '__main__':
    n=int(input().rstrip())
    d, v = tuple(int(x)-1 for x in input().rstrip().split())
    r=int(input().rstrip())
    a=[Trip(n) for _ in range(n)]

    for _ in range(r):
        i, to, j, td = tuple(int(x) for x in input().rstrip().split())
        i-=1
        j-=1
        a[i].add_point(to,td,j)
    print(_min_path(a, d, v))

