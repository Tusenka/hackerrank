#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=16&id_topic=21&id_problem=110
import sys
M=10**9
def _bfs(i, j, a, visited):
    visited[i][j]=True
    queue = [(i,j)]

    while queue:
        i,j=queue.pop(0)
        if i<len(a)-1 and a[i+1][j]==1:
            _mark_queue(queue, visited, (i+1),j)
        if i>0 and a[i-1][j]==1:
            _mark_queue(queue, visited, (i-1),j)
        if j<len(a[0])-1 and a[i][j+1]==1:
            _mark_queue(queue, visited, i,(j+1))
        if j>0 and a[i][j-1]==1:
            _mark_queue(queue, visited, i,(j-1))

def _mark_queue(queue, visited, i, j):
    if not visited[i][j]:
        visited[i][j] = True
        queue.append((i, j))


if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    n, m = tuple(int(x) for x in input().rstrip().split())
    a=[]
    a.extend(tuple(1 if x=='*' else 0 for x in input().rstrip()) for _ in range(n))
    visited=[[False for _ in range(m)] for _ in range(n)]
    _count=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and a[i][j]==1:
                _bfs(i, j, a, visited)
                _count+=1
    print(_count)