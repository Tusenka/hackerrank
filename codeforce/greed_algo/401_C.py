def solve(n: int, m: int):
    ans = [-1] * (n + m)

    if n > (m // 2) + 2:
        return [-1]

    if m > n * 2 + 4:
        return [-1]

    if n > m:
        ans[0] = 0
        n -= 1
    else:
        ans[0] = 1
        m -= 1

    for i in range(1, n + m + 1):
        if ans[i - 1] == 0 and m == 0:
            return [-1]
        if ans[i - 1] == 1 and i > 1 and ans[i - 2] and n == 0:
            return [-1]

        if ans[i - 1] == 0:
            ans[i] = 1
            m -= 1
            continue

        if i > 1 and ans[i - 2] == 1:
            ans[i] = 0
            n -= 1
            continue

        if m > n:
            ans[i] = 1
            m -= 1
            continue

        ans[i] = 0
        n -= 1

    return ans


n, m = tuple(map(int, input().split()))
print(*solve(n, m), sep="")
