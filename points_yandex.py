from collections import defaultdict


def solve(a: list[tuple[int,int]]):
    h=defaultdict(set)

    for p in a:
        h[p[0]].add(p[1])

    imin=-1
    v=None

    #if len(h) * len(h)>n: v=h[0] if len(h[0])==1 else (max(h[0])-min(h[0]))/2 - small optimization

    for x in h.keys():
       if len(h[x])==1:
          v=list(h[x])[0]
          break

       if imin==-1 or len(h[imin])>len(h[x]):
          imin=x

    v=v if v is not None else (max(h[imin]) + min(h[imin]))/2

    for i in h.keys():
        for s in h[i]:
            if s>v:
                continue
            if s==int(v):
                continue

            if int((v-s)+v) not in h[i]:
                return None

    return v


n=int(input())
a=[(0, 0)] * n

for i in range(n):
    p=tuple(map(int, input().split()))
    a[i]=(p[1], p[0])

print(solve(a=a))
