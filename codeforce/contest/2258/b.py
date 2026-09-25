from collections import defaultdict


def solve(a:list[int], m: int):
    a.sort()
    h=defaultdict(int)

    if len(a)==1:
       return 1 if a[0]%2 else 2

    for x in a:
        if not x%2:
            h[x]+=1

    v=[]
    for i,x in h.items():
       v.append((x,i))

    if not v:
       return len(a)

    v.sort(key=lambda x: (-x[0], x[1]))

    ans=len(a)

    for x in v:
        if x[0]*2>x[1]//2:
           ans=max(ans, x[0]*2+len(a)-1-x[1]//2)

    return ans



t=int(input())

for _ in range(t):
    n,m=tuple(map(int, input().split()))

    a=list(map(int,input().split()))

    print(solve(a=a, m=m))