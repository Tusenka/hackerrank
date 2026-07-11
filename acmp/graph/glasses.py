
def _solve(n: int):
    _dp=[[0 for _ in range(3)] for _ in range(n)]
    for i in range(n):
        _dp[i][0]=_dp[i-10]
        for j in range(3):

