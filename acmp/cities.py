import sys
def _dfs( a0 , a , visited, c ):
    visited[a0]=True
    yield a0+1
    for a1 in a[a0]:
        if not visited[a1]:
            yield from _dfs( a1 , a , visited )
    return True

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    (n, m) = tuple(int(x) for x in input().rstrip().split())
    a=[[0 for _ in range(0)] for _ in range(n)]
    for _ in range(m):
        x = tuple(int(x) for x in input().rstrip().split())
        a[x[0]-1].append(x[1]-1)
        a[x[1]-1].append(x[0]-1)
    k=int(input())
    c = {int(input().rstrip())-1 for _ in range(k)}
    visited= [ False ] * n
    _res=[]
    _res.extend(_dfs(x, a, visited , c) for x in c)
    for x in _res:
        print(len(x))
        print(*x)



