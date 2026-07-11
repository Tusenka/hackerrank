def solve(n: int):
    dp=[1]*(n+1)
    dp[1]=1
    dp[2]=2
    dp[3]=2

    for i in range(4, n+1):
        if not i%2:
           dp[i]=dp[i//2]+dp[i-2]
        else:
           dp[i]=dp[i-1]

    return dp[-1]




t=int(input())

print(solve(t))
