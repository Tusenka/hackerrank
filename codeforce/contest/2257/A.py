from collections import defaultdict


def solve(s:list[str], abbr:list[str]):
    h=defaultdict(int)
    for x in s:
        h[x[0].upper()]+=1

    for r in abbr:
        for x in r:
            if not h[x]:
                return False
    return True

t=int(input())

for i in range(t):
    n,m=list(map(int, input().split()))
    s=[]
    for _ in range(n):
       s.append(input())
    abbr=[]
    for _ in range(m):
       abbr.append(input())
    print("Yes" if solve(s=s, abbr=abbr) else "No")

