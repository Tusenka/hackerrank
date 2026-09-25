from collections import deque


def solve(a, x, y):
    if x>y:
       x,y=y,x

    bc=[ False for _ in range(len(a))]
    graph=[]
    for i in range(len(a)-x):
        if bc[i]:
           continue
        graph.append(set())
        q=deque()
        q.append(i)

        while True:
            j=q.popleft()
            if j in graph[-1]:
               break
            graph[-1].add(j)
            if x-j>=0:
                q.append(x-j)
            if y-j>=0:
                q.append(y-j)
            if x+j>=len(a):
                q.append(j+x)
            if j+y<len(a):
                q.append(j+y)


    hash_=[0]*len(a)
    for i, x in enumerate(graph):
        for v in x:
            hash_[v]=i

    as_=sorted([(a[i], i) for i in range(len(a))])
    for j, x in enumerate(as_):
        if hash_[j]!=hash_[x[1]]:
            return False
    return True


t=int(input())

for _ in range(t):
    n,x,y=list(map(int, input().split()))
    a=list(map(int, input().split()))

    print("YES" if solve(a, x, y) else "NO")