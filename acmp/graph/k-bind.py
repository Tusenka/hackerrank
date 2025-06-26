#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=52&id_problem=1181
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
    i,j=tuple(int(x)-1 for x in input().rstrip().split())
    a[i][j]=0
    a[j][i]=min(a[j][i], 1)

dp=floyd(a)
k=max(max(x) for x in dp)
print(k)
    

