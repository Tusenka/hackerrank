#https://codeforces.com/group/sNzo7JKQN1/contest/527247/problem/A
import heapq

M=10**9
def dejkstra(a: list, s: int):
    res=[M]*len(a)
    transfer=[0]*len(a)
    visited = [False]*len(a)
    work=[(0,s)]
    res[s]=0
    while work:
        q=heapq.heappop(work)

        if visited[q[1]]:
            continue

        visited[q[1]] = True
        for e in a[q[1]]:
            if res[q[1]]+e[0]<res[e[1]]:
                heapq.heappush(work, e)
                res[e[1]]=e[0]+res[q[1]]
                transfer[e[1]]=q[1]


    return res, transfer


def cound_points_on_roads(a: list[int], r: int, es: list ):
    count=0
    for i, x in enumerate(a):
        if x<r:
           for e in es[i]:
               if x+e[0]>r:
                    count+=1
    return count


def solve(a:list, s:int, l:int):
    res, transfer=dejkstra(a, s=s)
    cities=len([x for x in res if x==l])
    roads=cound_points_on_roads(a=res, r=l, es=a)

    return cities+roads


n, k, s = tuple(map(int, input().rstrip().split()))
a=[list() for _ in range(n)]

for _ in range(k):
    i, j, v = tuple(map(int,input().rstrip().split()))
    a[i-1].append((v, j-1))
    a[j-1].append((v, i - 1))

l=int(input())

print(solve(a=a,s=s-1, l=l))
