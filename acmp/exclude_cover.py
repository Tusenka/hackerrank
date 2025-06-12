def _dfs( a0 , a , visited ):
    visited[a0]=True
    yield a0+1
    for a1 in a[a0]:
        if a1 not in visited:
            _dfs(a1, a, visited)
    return True
    
if __name__ == '__main__':
    (n, m) = tuple(int(x) for x in input().rstrip().split())
    _data=[set() for _ in range(m*n)]
    
    for i in range(n):
        x = input().rstrip()
        for j in range(m):
            _data[i*m+j] = { i * m + j } if x[j]=='#' else set()
    for i in range(n-1):
        for j in range(m):
            if len(_data[(i+1)*m+j])>0:
                _data[i*m+j].add((i+1)*m+j)
                _data[(i+1)*m+j].add(i*m+j)

    to_visit=[False] * n
    _count=0
    while len(to_visit)>0:
        i=to_visit.pop()
        _count+=1
        _dfs(i, a, to_visit)
        
        
    
