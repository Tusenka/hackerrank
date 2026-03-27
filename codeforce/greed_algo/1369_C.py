# https://codeforces.com/problemset/problem/1369/C


def solve(a: list[int], w: list[int]):
    a.sort()
    w.sort()
    ans = 0
    l = 0
    r = len(a) - 1
    for x in w:
        if x == 1:
            ans += 2 * a[r]
            r -= 1
            continue
        ans += a[l] + a[r]
        l += x - 1
        r -= 1

    return ans


t = int(input())

for _ in range(t):
    n, k = tuple(map(int, input().split()))

    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    print(solve(a, w))
