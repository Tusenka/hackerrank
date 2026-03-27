from collections import defaultdict


def solve(a: list[int]):
    h=defaultdict(set)
    for i,v in enumerate(a):
        h[v].add(i)

    is_=set()
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
           is_.add(i)

    for i in is_:
        k=len(a)-i-1
        if k>=len(a):
           continue

        if (k>0 and a[k-1]==a[i]) or (k<len(a)-1 and a[k+1]==a[i]):
            continue

        a[i], a[k]=a[k], a[i]

    _ans=0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
           _ans+=1

    return _ans




t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a))
