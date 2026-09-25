def solve(c: list[int]):
    c.sort()

    if c[-1]==1:
       return 0

    if sum(c)<3:
        return 0

    ind=[x for x in c if x>=2]
    ans=sum(ind)
    rest=len(c)-len(ind)
    for x in ind:
        if not rest:
            break
        v=min(rest,(x//2)-1)
        ans+=v
        rest-=v

    if len(ind)==1 and rest>0:
        ans+=1
    return ans



t=int(input())

for _ in range(t):
    input()
    c=list(map(int, input().split()))
    print(solve(c))
