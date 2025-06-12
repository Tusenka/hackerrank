#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=15&id_topic=16&id_problem=88


def _eval_game(a):
    n=len(a)
    _dp=[[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        _dp[j][j]=a[j]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            _dp[i][j]=max(a[i]-_dp[i+1][j], a[j]-_dp[i][j-1])
    return 1 if _dp[0][-1]>0 else 0 if _dp[0][-1]==0 else 2

_=int(input())
seq=list([int(x) for x in input().split()])
print(_eval_game(seq))
