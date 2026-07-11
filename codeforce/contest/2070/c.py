
def check(st: list[int] ,c:list[int], v:list[int], x: int, k: int):
    dc=[c[i] for i in range(len(v)) if v[i]>x]
    dv=[v[i] for i in range(len(v)) if v[i]>x]

    for i,x in c:
        if c==1:








def solve(c: list[int], v: list[int]):
    cv=[(v[i] if c[i]==1 else 0,i) for i in range(len(c))]


t=int(input())

for t in range(t):
    n,k=tuple(map(int, input().split()))
    c=list(map(lambda x: 1 if x=='B' else 0, input()))
    v=list(map(int, input().split()))

    print(solve(c=c, v=v))
