#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=16&id_topic=22&id_problem=118
def _shocko(n: int):
    if n%2:
        return 0
    _dp=[0]*(n+1)
    _dp[0]=1
    _dp[2]=3

    for i in range(4,n+1,2):
        _dp[i]=3*_dp[i-2]
        for j in range(i-4, -1, -2):
            _dp[i]+=(_dp[j]<<1)
    return _dp[-1]

n=int(input())
print(_shocko(n))