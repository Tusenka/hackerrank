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
#        если a ≤ 0 или b ≤ 0 или c ≤ 0, то F(a, b, c) = 1#
#        если a > 20 или b > 20 или c > 20, то F(a, b, c) = F(20, 20, 20)
#        если a < b и b < c, то F(a, b, c) = F(a, b, c-1) + F(a, b-1, c-1) - F(a, b-1, c)
#        иначе F(a, b, c) = F(a-1, b, c) + F(a-1, b-1, c) + F(a-1, b, c-1) - F(a-1, b-1, c-1)


if __name__ == '__main__':
    (a, b, c) =  tuple([int(x) for x in input().rstrip().split()])
    print(fib(a, b, c))
