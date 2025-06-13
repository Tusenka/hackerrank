#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=50&id_problem=1217
import sys
def _dfs( a0, a: list, visited: list, c: set):
    visited[a0]=True

    yield a0+1

    for a1 in a[a0]:

        if not visited[a1] and a1 not in c:
            yield from _dfs( a1 , a , visited, c)

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    (n, m) = tuple(int(x) for x in input().rstrip().split())
    a=[[0 for _ in range(0)] for _ in range(n)]

    for _ in range(m):
        x = tuple(int(x) for x in input().rstrip().split())
        a[x[0]-1].append(x[1]-1)
        a[x[1]-1].append(x[0]-1)

    k=int(input())
    c = {int(x)-1 for x in input().rstrip().split()}
    visited= [ False ] * n
    _res=dict(zip(sorted(c), [ list(_dfs(x, a, visited , c)) for x in sorted(c)]))

    for x in sorted(c):
        print(len(_res[x]))
        print(*_res[x])



