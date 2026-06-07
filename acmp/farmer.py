def solve(a: list):
    dp=[[0 for _ in range(t)] for _ in range(t)]
    dp[-1][-1]=a[-1][-1]
    dp[-1][-2]=a[-1][-2]
    dp[-2][-1]=a[-1][-2]

    for i in range(len(a)-2, -1, -1):
        for j in range(len(a)-2, -1, -1):
            if a[i][j]:
                m=min(dp[i+1][j+1], dp[i+1][j], dp[j][i+1])+1
                for k in range(i, m+1, 1):
                    if a[i][k]==0:
                        m=min(k-i, m)
                        break
                    if a[k][j]==0:
                        m=min(k-i, m)
                        break

                dp[i][j]=m

    m=max(max(x) for x in dp)

    return m*m




t=int(input())

a=[[0 for _ in range(t)] for _ in range(t)]

for i in range(t):
    a[i]=list(map(int, input()))

print(solve(a=a))
