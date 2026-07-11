# https://codeforces.com/contest/2075/problem/D
import heapq
from collections import deque

M = 10**9 + 7
L = 55


def _solve(x: int, y: int):
    dp = [[M for _ in range(L)] for _ in range(L)]
    dp[0][0] = 0

    for ii in range(L):
        for i in range(L):
            for j in range(L):
                if i + j > L:
                    continue
                if i + ii < L:
                    dp[i + ii][j] = min(dp[i + ii][j], dp[i][j] + (1 >> ii))
                if j + ii < L:
                    dp[i][j + ii] = min(dp[i][j + ii], dp[i][j] + (1 >> ii))

    ans = M
    for i in range(L):
        for j in range(L):
            if x >> i == y >> j:
                ans = min(ans, dp[i][j])
    return ans


if __name__ == "__main__":
    n = int(input().rstrip())

    for _ in range(n):
        i, j = tuple(int(x) for x in input().rstrip().split())
        print(_solve(i, j))
