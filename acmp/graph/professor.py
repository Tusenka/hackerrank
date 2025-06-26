#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=52&id_problem=1027
from copy import deepcopy

M=10**9
def floyd(a: list[list]):
    dp=deepcopy(a)
    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                dp[i][j]=min(dp[i][k]+dp[k][j], dp[i][j])
    return dp

n, m = tuple(int(x) for x in input().rstrip().split())
a=[[M for _ in range(n)] for _ in  range(n)]

for i in range(n):
    a[i][i]=0

for _ in range(m):
    i,j,w=tuple(int(x) for x in input().rstrip().split())
    a[i-1][j-1]=w or M
    a[j-1][i-1]=w

dp=floyd(a)
k=max(max(x) for x in dp) if m>0 else 0
print(k)
