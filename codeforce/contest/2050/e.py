def solve(a:str, b: str, c: str):
    dp=[[len(c) for _ in range(len(b))] for _ in range(len(a))]

    for i in range(1, len(a)):
        if a[i] in c:
           dp[i][0]=dp[i-1][0]-1
        else:
           for j in range(i, len(a)):
               dp[j][0]=dp[i-1][0]
           break

    for i in range(1, len(b)):
        if b[i] in c:
            dp[0][i]=dp[0][i-1]-1
        else:
            for j in range(i, len(a)):
                dp[0][i]=dp[0][i-1]
            break

    for i in range(1,len(a)):
        if a[i] not in c[i:]:
            break
        for j in range(i, min(len(b), len(c)-i)):
            if b[j] not in c[j:]:
                break
            dp[i][j]=min(dp[i-1][j]-1, dp[i][j-1]-1)

    return dp[-1][-1]

t=int(input())

for _ in range(t):
    a=input()
    b=input()
    c=input()

    print(solve(a,b,c))