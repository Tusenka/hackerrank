def solve(res, l, r):
    return res[r + 1] - res[l]


def prepare(a: list, b: list):
    res = [0] * (len(a) + 1)
    last = -1
    for i in range(len(a) - 1, -1, -1):
        if a[i] < b[i]:
            a[i] = b[i]

        if a[i] < last:
            a[i] = last

        last = a[i]

    res[0] = 0
    res[1] = a[0]
    for i in range(len(a)):
        res[i + 1] = res[i] + a[i]

    return res


t = int(input())

for _ in range(t):
    n, q = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = prepare(a, b)
    ans = [0] * q
    for i in range(q):
        l, r = tuple(map(int, input().split()))
        ans[i] = solve(res, l - 1, r - 1)

    print(*ans)
