def fib(aa, bb, cc):
    if aa<=0 or bb<=0 or cc<=0:
        return 1
    if aa>20 or bb>20 or cc>20:
        return fib(20, 20, 20)
    _dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    for a in range(1, aa+1):
        for b in range(1, bb+1):
            for c in range(1, cc+1):
                if a<b<c:
                    _dp[a][b][c]=_dp[a][b][c -1]+_dp[a][b-1][c -1]-_dp[a][b-1][c]
                else:
                    _dp[a][b][c]=_dp[a-1][b][c] + _dp[a-1][b-1][c] + _dp[a-1][b][c-1] - _dp[a-1][b-1][c-1]
    return _dp[aa][bb][cc]


if __name__ == '__main__':
    (a, b, c) =  tuple([int(x) for x in input().rstrip().split()])
    print(fib(a, b, c))
