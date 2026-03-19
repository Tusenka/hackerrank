# https://codeforces.com/contest/2127/problem/B
def solve(a, x):
    r = 1

    if all(x == 0 for x in a):
        return 1

    for i in range(x + 1, len(a)):
        r += 1 if a[i] == 0 or all(x == 1 for x in a[i + 1 :]) else 2

    l = 1

    for i in range(x - 1, -1, -1):
        l += 1 if a[i] == 0 or all(x == 1 for x in a[:i]) else 2

    if len([1 for i in a[:x] if i == 1]) == len([1 for i in a[x + 1 :] if i == 1]):
        return max(min(l, r) - 1, 1)

    else:
        return min(l, r)


t = int(input().rstrip())

for _ in range(t):
    _, i = tuple(int(x) - 1 for x in input().rstrip().split())
    a = list(0 if x == "." else 1 for x in input().rstrip())
    print(solve(a, i))
