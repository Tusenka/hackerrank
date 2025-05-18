from functools import lru_cache


def _triangle(a):
    _dp=[[ 0 for _ in range(len(a))] for _ in range(len(a))]
    for k in range(2, len(a)):
        for i in range(len(a)-k):
            _max=0
            for j in range(i+1, i+k):
                _cost=a[i]*a[i+k]*a[j]+_dp[i+1][j-1]+_dp[j+1][i+k-1]
                if _cost>_max:
                    _max=_cost
                _cost=_dp[i][j-1]+_dp[j][i+k]
                if _cost>_max:
                    _max=_cost
            _cost=_dp[i][i+k-1]+_dp[i+k][i+k]
            if _cost>_max:
                _max=_cost
            _dp[i][i+k]=_max
    return _dp[0][-1]



q = int(input().strip())

for q_itr in range(q):
    _ = input().rstrip()
    a = tuple([int(x) for x in input().rstrip().split()])
    result = _triangle(a)
    print(result)