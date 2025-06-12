import sys


def _dfs( a0 , a , visited , result = None ):
    if result is None :
        result = [ ]
    visited[a0]=True
    result.append(a0+1)
    for a1 in a[a0]:
        if not visited[a1]:
            _dfs( a1 , a , visited, result )
    return result
    
if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    (n, m) = tuple(int(x) for x in input().rstrip().split())
    a=[[0 for _ in range(0)] for _ in range(n)]
    for _ in range(m):
        x = tuple(int(x) for x in input().rstrip().split())
        a[x[0]-1].append(x[1]-1)
        a[x[1]-1].append(x[0]-1)
    visited= [ False ] * n
    _count=0
    for i in range(n):
        if not visited[i]:
            _dfs( i , a , visited )
            _count+=1
    print(_count)
    
    visited= [ False ] * n
    for i in range(n):
        if not visited[i]:
            _res= _dfs( i , a , visited )
            print(len(_res))
            print(*_res)
        
        
    
