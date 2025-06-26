#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=51&id_problem=654

import sys
M=10**9
def _bfs(x, n=8, m=8):
    d=[[M for _ in range(m)] for _ in range(n)]
    queue = [(x[0],x[1])]
    d[x[0]][x[1]]=0
    while queue:
        i,j=queue.pop(0)
        steps=[]
        for ii in (i+2, i-2):
            steps.extend((ii, jj) for jj in (j+1, j-1))
        for ii in (i+1, i-1):
            steps.extend((ii, jj) for jj in (j+2, j-2))
        steps = (step for step in steps if 0<=step[0]<n and 0<=step[1]<m)
        for step in steps:
            _mark_queue(queue=queue, step=step, o=(i,j),  d=d )
    return d

def _mark_queue(queue, step, o, d):
    if d[step[0]][step[1]]==M:
        queue.append(step)
        d[step[0]][step[1]]=d[o[0]][o[1]]+1


import itertools
if __name__ == '__main__':
    p1, p2 = tuple(input().rstrip().split())
    p1=(ord(p1[0])-ord('a'), int(p1[1])-1)
    p2=(ord(p2[0])-ord('a'), int(p2[1])-1)
    d1=_bfs(p1)
    d2=_bfs(p2)
    _min=M
    d=[d1[i][j]+d2[i][j] for i in range(8) for j in range(8) if (d1[i][j]+d2[i][j])%2==0]
    _min=min(d)//2 if len(d) else -1
    print(_min)