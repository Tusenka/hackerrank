import sys

M = 10 ** 9 + 9


def _solve(n):
    _dp=[1]*(3)
    _dp[0]=0
    _dp[1]=1
    for i in range(3, n+1):
        _dp[2]=((_dp[1]+_dp[0])*(i-1)) % M
        _dp[0]=_dp[1]
        _dp[1]=_dp[2]
    return _dp[-1] % (M)
sys.set_int_max_str_digits(100000)
n=int(input())
print(_solve(n))