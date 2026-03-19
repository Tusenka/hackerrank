# https://codeforces.com/problemset/problem/2167/G
from copy import copy

M = 10**9


def solve(a: list, c: list):
    anew = copy(a)
    dp = [0] * len(a)

    for i in range(1, len(a)):
        if anew[i - 1] > anew[i]:
            dp_last = 0
            j = i - 1

            while j >= 0:
                if anew[j] <= anew[i]:
                    break
                else:
                    dp_last += c[j]
                j -= 1

            j = max(0, j)
            if dp_last <= c[i]:
                dp[i] = dp_last + dp[j]
                anew[i - 1] = a[j]
            else:
                dp[i] = dp[i - 1] + c[i]
                anew[i] = anew[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[-1]


t = int(input())
for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = solve(a, c)
    print(ans)
