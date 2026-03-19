# https://codeforces.com/contest/2153/problem/C

M = 10**9 + 7


def solve(a: list) -> int:
    a.sort()
    W = sum(a) // 2 + 1
    dp = [[0 for _ in range(W + 1)] for _ in range(W + 1)]
    visited = [False for _ in range(len(a))]
    dp[0][0] = M
    for i in range(len(a)):
        _break = False
        for w1 in range(W):
            for w2 in range(W):
                if (w1 - a[i] >= 0 and dp[w1 - a[i]][w2]) or (
                    w2 - a[i] >= 0 and dp[w1][w2 - a[i]]
                ):
                    dp[w1][w2] = i + 1
                    _break = True
                    visited[i] = True
            if _break:
                break
        if _break:
            continue
    _count = len(list(filter(lambda x: x, visited)))
    for w in range(W, 1, -1):
        if dp[w][w] != 0:
            _max = max(
                [a[i] for i in range(len(a)) if not visited[i] and a[i] != 2 * w] + [0]
            )
            if _count == 2 and _max < 0:
                return 0
            return w * 2 + _max

    return 0


t = int(input().rstrip())

for _ in range(t):
    _ = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(solve(a))
