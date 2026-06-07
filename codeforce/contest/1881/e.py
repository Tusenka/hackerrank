def solve(a: list[int]):
    if len(a)==1:
        return 1

    dp=[0]*(len(a)+1)
    dp[-2]=1
    dp[-3]=0 if a[-2]==1 else 2

    #2 1 1 8 3 1 1 1
    for i in range(len(a)-3, -1, -1):
        dp[i]=min(dp[i+1]+1, dp[a[i]+i+1] if a[i]+i+1<=len(a) else len(a)-i+1)

    return min(dp[x]+x for x in range(min(a[0], len(dp))))

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a=a))