M=10**9
def solve(a: list):
    dp=[[M for _ in range(len(a)+1)] for _ in range(len(a))]
    dp[0][1]=0

    if len(a)==1:
        return 1

    for i in range(1, len(dp)):
        dp[i][1]=i if a[dp[i-1][1]]<a[i] else dp[i-1][1]

    for k in range(1, len(a)):
        for s in range(2, len(a)+1):
            if dp[k-1][s-1]<M and a[dp[k-1][s-1]]<a[k]<(a[dp[k-1][s]] if dp[k-1][s]<M else M):
               dp[k][s]=k

            else:
               dp[k][s]=dp[k-1][s]

    ans=1
    for s in range(2, len(a)+1):
        if dp[-1][s]<M:
           ans=max(ans,s)
        else:
           break

    return ans
    # j=-1
    # for i in range(ans, 0, -1):
    #     yield a[dp[j][i]]
    #     j=dp[j][i]
    #
input()
a =list(map(int, input().split()))


print(solve(a))