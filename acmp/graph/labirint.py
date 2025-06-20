#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=51&id_problem=654

import sys
M=10**9
def _min_path(x, y, a):
    n=len(a)
    m=len(a[0])
    d=[[M for _ in range(m)] for _ in range(n)]
    queue = [(x[0],x[1])]
    d[x[0]][x[1]]=0
    while queue:
        i,j=queue.pop(0)
        steps=[]
        if i<len(a)-1: steps.append((i+1,j))
        if j<len(a[0])-1: steps.append((i,j+1))
        if i>0: steps.append((i-1,j))
        if j>0: steps.append((i,j-1))
        for step in steps:
            if a[step[0]][step[1]]==1:
                _mark_queue(queue=queue, step=step, o=(i,j),  d=d )
            if step==y:
                break
    return d[y[0]][y[1]]

def _mark_queue(queue, step, o, d):
    if d[step[0]][step[1]]==M:
        queue.append(step)
        d[step[0]][step[1]]=min(d[step[0]][step[1]], d[o[0]][o[1]]+1)


if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    n, m = tuple(int(x) for x in input().rstrip().split())
    a=[]
    t=()
    for i in range(n):
        a.append([])
        for j, x in enumerate(input().rstrip()):
            a[-1].append(0 if x=='#' else 1)
            if x=='T':
                t=(i,j)
    _count=0
    td=_min_path(t, (n-2, m-2), a)
    d=_min_path((1,1), (n-2, m-2), a)
    print(d)
    if td<=d:
        print("No")
    else:
        print("Yes")