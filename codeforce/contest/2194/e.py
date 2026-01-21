from copy import copy, deepcopy

M=10**9+7

def solve(a:list[list[int]]):
    n=len(a)
    m=len(a[0])

    dp=optimal_dp(a)
    path=optimal_path(dp,a)

    min_=M
    if all(a[p[0]][p[1]]<=0 for p in path):
        assert False, "TODO::"

    for ii in range(0, m):
        aa=deepcopy(a)
        i,j=path[ii]
        if a[i][j]<=0:
           continue

        aa[i][j]=-a[i][j]
        dp=optimal_dp(aa)
        if dp[-1][-1]<min_:
            min_=dp[-1][-1]

    return min_



def optimal_dp(a: list[list[int]]):
    n=len(a)
    m=len(a[0])

    dp=[[0 for _ in range(m)] for _ in range(n)]
    dp[0][0]=a[0][0]
    for i in range(0,n):
        for j in range(0,m):
            if i==0 and j==0:
                continue
            dp[i][j]=max(dp[i-1][j] if i>0 else -M, dp[i][j-1] if j>0 else -M)+a[i][j]
    return dp

def optimal_path(dp: list[list[int]], a: list[list[int]]):
    i=n-1
    j=m-1
    ii=m-2

    path=[tuple()]*m
    path[m-1]=(n-1,m-1)
    while ii>0:
        if i>0 and dp[i-1][j]==dp[i][j]-a[i][j]:
            path[ii]=(i-1,j)
            i-=1
        elif j>0 and dp[i][j-1]==dp[i][j]-a[i][j]:
            path[ii]=(i,j-1)
            j-=1
        else:
            assert False, "wrong dp {path}"
        ii-=1
    path[ii]=(0,0)

    return path


t=int(input())
for _ in range(t):
    n,m=tuple(map(int,input().split()))

    a=[]
    for _ in range(n):
        a.append(list(map(int,input().split())))

    print(solve(a))