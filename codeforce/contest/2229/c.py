M=10**9

def solve(a: list[int]):
    ps=[0 for _ in range(len(a))]
    ps[0]=a[0]

    for i in range(1, len(a), 1):
        ps[i]=ps[i-1]+abs(a[i])

    sf=[0 for _ in range(len(a))]
    sf[-1]=a[-1]

    for i in range(len(a)-2, -1, -1):
        sf[i]=a[i]+sf[i+1]

    imax=-1
    max_=sum(a)

    for i in range(1, len(a), 1):
        if a[i]>0 and sf[i]+ps[i-1]-a[i]>max_:
           imax=i
           max_=sf[i]+ps[i-1]-a[i]

    if imax==-1:
        return []

    pos=[]
    for j in range(imax-1, -1, -1):
        if len(pos)&1:
           a[j]=-a[j]
        if a[j]>0:
           pos.append(j+1)

    pos.append(imax+1)

    return list(pos)

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))
    ans=solve(a)
    print(len(ans))
    print(*ans)



