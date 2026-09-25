import heapq


def solve(a: list[tuple[ int, int, int]], n):
    if len(a)==0:
        return 24*60*60

    events=[]

    for x in a:
        events.append((x[0],0))
        events.append((x[1],1))

    events.sort()
    start=-1
    o=0
    ans=0
    for x in events:
        if  x[1]==0:
            start=x[0]
            o+=1
        else:
            if o>=n:
                ans+=x[0]-start
            o-=1
    return ans

n=int(input())
a=[]
m=n
for i in range(n):
    raw=tuple(map(int, input().split()))
    start = raw[0] * 60 * 60 + raw[1] * 60 + raw[2]
    end = raw[3] * 60 * 60 + raw[4] * 60 + raw[5]
    if start<end:
        a.append((start, end, -1))
    if start>end:
        a.append((start, 24*60*60, -1))
        a.append((0, end, start))
    if start==end:
        m-=1


print(solve(a=a, n=m))