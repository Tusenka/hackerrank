from functools import cache

M = 10 ** 9 + 7

def _build_coins(a: tuple, i: int):
    if len(a)==0:
        yield 0, 0
        return
    if i == len(a) - 1:
        yield 0, 0
        yield a[-1], 1
        yield a[-1] * 2, 2
        return
    for x in _build_coins(a, i + 1):
        yield x[0], x[1]
        yield x[0] + a[i], x[1] + 1
        yield x[0] + 2 * a[i], x[1] + 2


def two_nulls(n: int, k: int):
    _dp=[[0 for _ in range(2)] for _ in range(n+1)]
    _dp[1][0]=0
    _dp[1][1]=k-1
    for i in range(2, n+1):
        _dp[i][0]=_dp[i-1][1]
        _dp[i][1]=_dp[i-1][1]*(k-1)+_dp[i-1][0]*(k-1)
    return _dp[n][1]+_dp[n][0]

if __name__ == '__main__':
    (n, k) = tuple([int(x) for x in input().rstrip().split()])
    print(two_nulls(n, k))
