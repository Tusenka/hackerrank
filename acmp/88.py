def solve(a: list):
    dp=[[0 for _ in range(len(a))] for _ in range(len(a))]
    sign=-1 if len(a)//2 else 1

    for i in range(len(a)-1):
        dp[i][i+1]=max(a[i],a[i+1])*sign
        dp[i+1][i]=max(a[i], a[i+1])*sign

    for i in range(len(a)-1, -1, -1):
        for j in range(i+1, len(a)):
            dp[i][j]=max(a[j]+dp[i][j-1], a[i]+dp[i+1][j]) if (i+j)%2==len(a)%2 else -max(a[j]-dp[i][j-1], a[i]-dp[i+1][j])

    return 0 if dp[0][-1]==0 else 1 if dp[0][-1]*sign>0 else 2

input()
a=list(map(int, input().split()))

print(solve(a))