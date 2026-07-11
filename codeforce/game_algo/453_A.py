def solve(m: int, n: int):
    _ps = 0
    ans = 0
    p = m**n
    for i in range(m, -1, -1):
        val = 1 - ((i - 1) ** n - _ps) / p
        _ps += val
        ans += val * i

    return ans


m, n = tuple(map(int, input().split()))
print(solve(m, n))
