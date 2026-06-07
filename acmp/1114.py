M=10**9

def binary_search(d, v):
    r=len(d)-1
    l=0

    while r>l+1:
          m=(r+l)//2
          if d[m]>v:
             r=m
          else:
             l=m

    return r


def solve(n, a0, k, b, m):
    n=min(n, m*2)
    a=[a0]*n

    for x in range(1, n):
        a[x]=(a[x-1]*k+b) % m

    dp=[M for _ in range(len(a)+1)]
    dp[0]=-M
    dp[1]=0
    prev=[-1] * (len(a))

    for k in range(1, len(a)):
        j=binary_search([a[i] if M > i >= 0 else i for i in dp], a[k])
        if (dp[j-1]<M and (dp[j-1]<0 or a[dp[j-1]]<a[k])) and j<len(dp)-1 and (dp[j]==M or a[k]<a[dp[j]]):
            dp[j]=k
            prev[k]=max(dp[j-1], 0)
            

    ans=1
    for s in range(len(dp)-1, -1, -1):
        if dp[s]<M:
           ans=s
           break

    i=dp[ans]

    while i>=0:
        yield a[i]
        i=prev[i]


# dp[i][j]=min(dp[i][j-1] - bool(b[j-1] in c), dp[i-1][j]-bool(a[i-1] in c))

# dp[0][0]=len(c)
# dp[0][1]=dp[0][0]-bool(b[0] in c)
# dp[1][0]=dp[0][0]-bool(a[0] in c)

# for i,j in

n, a0, k, b, m=tuple(map(int, input().split()))


print(*reversed(list(solve(n, a0, k, b, m))))