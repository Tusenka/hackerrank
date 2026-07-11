from collections import defaultdict


def solve(a:list):
    h=defaultdict(int)
    for x in a:
        h[x]+=1
    h=sorted(h.values(), reverse=True)
    _sum=h[0]
    last=h[0]
    for i in range(1,len(h)):
       if h[i]<last:
          _sum+=h[i]
          last=h[i]
          continue
       if last==0:
           break
       _sum+=last-1
       last=last-1

    return _sum

t=int(input())

for _ in range(t):
    _=int(input())
    a=list(map(int, input().split()))

    print(solve(a))
