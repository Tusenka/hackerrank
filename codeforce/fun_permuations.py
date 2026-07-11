# https://codeforces.com/contest/2137/problem/B?locale=en
def solve(a, k=3):
    ind = [-1] * len(a)
    unused = set(a)
    for i, x in enumerate(a):
        for y in unused:
            if (x + y) % k == 0:
                unused.remove(y)
                ind[i] = y
                break
    if unused:
        return solve(a, k + 1)
    else:
        return ind


t = int(input().rstrip())

for _ in range(t):
    _ = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    print(*solve(a))
