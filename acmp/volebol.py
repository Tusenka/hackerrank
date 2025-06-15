#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=16&id_topic=21&id_problem=110
import sys

a=[()]


def _bfs(a, visi):
    if parents is None:
        parents = {}
    visited[a0]=color
    x, y=None, None
    for a1 in a[a0]:
        if visited[a1]==color:
           return parents, a0, a1
        elif visited[a1]==-1:
           parents[a1]=a0
           _, x, y= _dfs(a1, a, visited, color ^ 1, parents)
    visited[a0]=2
    return parents, x, y

def _dfs(a0, a, visited, color=0, parents=None):
    if parents is None:
        parents = {}
    visited[a0]=color
    x, y=None, None
    for a1 in a[a0]:
        if visited[a1]==color:
           return parents, a0, a1
        elif visited[a1]==-1:
           parents[a1]=a0
           _, x, y= _dfs(a1, a, visited, color ^ 1, parents)
    visited[a0]=2
    return parents, x, y

def _recovery_dfs(parents, a0, a1):
    x=a0
    while x in parents and x!=a1:
        yield x+1
        x=parents[x]
    yield a1+1

if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    (n, m) = tuple(int(x) for x in input().rstrip().split())
    a=[[0 for _ in range(0)] for _ in range(n)]
    for _ in range(m):
        x = tuple(int(x) for x in input().rstrip().split())
        a[x[0]-1].append(x[1]-1)
    visited= [ -1 ] * n
    for i in range(n):
        if visited[i] == -1:
            _res, a0, a1=_dfs(i, a, visited)
            if a0:
                print(list(_recovery_dfs(parents=_res, a0=a0, a1=a1)))
                break
    else:
        print("No")