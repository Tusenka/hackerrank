# https://codeforces.com/contest/2163/problem/C
M = 10**9


def has_path(a, b, l, r):
    if a[0] < l or a[0] > r or b[-1] < l or b[-1] > r:
        return False

    for i in range(1, len(a)):
        if a[i] < l or a[i] > r:
            for j in range(i - 1, len(b)):
                if b[j] < l or b[j] > r:
                    return False
            else:
                return True

    return True


def solve(a: list, b: list):
    n = len(a)
    l = 1
    ans = 0

    while l <= n * 2:
        for t in range(l, 2 * n + 1):
            if has_path(a, b, l, t):
                ans += 2 * n - t + 1
                l += 1
                break
        else:
            break
    return ans


t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = solve(a, b)
    print(ans)
