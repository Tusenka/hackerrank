# https://codeforces.com/problemset/problem/44/E?locale=en


def solve(s: str, k: int, a: int, b: int):
    n = len(s)
    if a * k > n or b * k < n:
        return -1

    _dp = [a] * k
    rest = n - a * k
    x = b - a
    for i in range(k - 1, -1, -1):
        if rest - x >= 0:
            rest -= x
            _dp[i] = b
        else:
            _dp[i] = rest + a
            return _dp
    return _dp


k, a, b = tuple(int(x) for x in input().rstrip().split())
s = input().rstrip()

_dp = solve(s, k, a, b)
if _dp == -1:
    print("No solution")
else:
    x0 = 0
    for i, x in enumerate(_dp):
        print(s[x0 : x0 + x])
        x0 = x0 + x
