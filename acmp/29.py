def solve(a: list):
    dp=[[0 for _ in range(2)] for _ in range(len(a))]

    dp[-1][0]=abs(a[-2]-a[-1])
    dp[-1][1]=3*abs(a[-3]-a[-1])

    for i in range(len(a)-2, 0, -1):
        x=dp[i+1][0]

        if i+2<len(a)-1:
            x=min(x, dp[i+2][1])

        dp[i][0]=x+abs(a[i-1]-a[i])
        if i>1:
            dp[i][1]=x+3*abs(a[i-2]-a[i])

    return min(dp[1][0], dp[2][1])


t = int(input())

a = list(map(int, input().split()))
print(solve(a=a))
