def solve(a: list[int]):
    if a[0]==1:
       a=a[1:]

    if len(a)<=1:
        return 1

    dp=[0]*(a[-1]+1)
    for x in a:
        j=2
        dp[x]+=1
        while j*j<=x:
            if x%j==1:
               if dp[x//j]>dp[j]:
                   dp[x]=max(dp[x], dp[x//j]+1)
               else:
                   dp[x]=max(dp[j]+1, dp[x])
               dp[j]+=1
               dp[x//j]+=1
               x=x//j
            j+=1

    return max(dp)

input()

a=list(map(int, input().split()))
print(solve(a=a))
