# https://codeforces.com/contest/2148/problem/D


def solve(a):
    a.sort(key=lambda x: x, reverse=True)

    a1 = list([a[i] for i in range(len(a)) if a[i] % 2])
    a0 = list([a[i] for i in range(len(a)) if a[i] % 2 == 0])

    count_1 = len(a1)
    if count_1 == 0:
        return 0

    res = sum(a1[: count_1 // 2]) + sum(a0)
    if count_1 % 2 == 1:
        res += a1[count_1 // 2]
    return res


t = int(input().rstrip())

for _ in range(t):
    _ = input()
    a = list(map(int, input().rstrip().split()))
    print(solve(a))
