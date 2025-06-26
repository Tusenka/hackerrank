#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=52&id_problem=669

from copy import deepcopy

M=10**9
def floyd(a: list[list]):
    dp=deepcopy(a)
    for i in range(len(dp)):
        for j in range(len(dp)):
            for k in range(len(dp)):
                if dp[i][k]<M and dp[k][j]<M:
                    dp[i][j]=min(dp[i][k]+dp[k][j], dp[i][j])
    return dp

n= int(input().rstrip())
a=[[M for _ in range(n)] for _ in  range(n)]

for i in range(n):
    a[i] = [M if int(x)==0 else int(x) for x in input().rstrip().split()]

for i in range(n):
    a[i][i]=0

dp=floyd(a)
for x in dp:
    print(*[1 if 0<=v<M else 2 if v<0 else 0 for v in x ])