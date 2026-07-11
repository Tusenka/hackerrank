def solve(n: int, m: int, d: int):
    k = d // m + 1
    ans = n // k
    rest_n = n % k
    rest = rest_n
    if rest > d:
        return ans + solve(rest, m, d)
    elif rest > 0:
        return ans + 1
    else:
        return ans


t = int(input())

for _ in range(t):
    n, m, d = tuple(map(int, input().split()))

    print(solve(n, m, d))
